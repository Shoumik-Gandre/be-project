
import json
import os
from typing import Dict, Any, List
import azure.cognitiveservices.speech as speechsdk
from pydub import AudioSegment
from dotenv import load_dotenv



class AzureSpeechUtils:

    def __init__(self, api_key: str, region: str):
        self.api_key = api_key
        self.region = region
        self.speech_config = speechsdk.SpeechConfig(
            subscription=self.api_key, region=self.region)
        self.speech_config.request_word_level_timestamps()

    def get_milliseconds(self, time: float) -> float:
        """converts time in nanoseconds to milliseconds"""
        return time / 10000


class SpeechToText(AzureSpeechUtils):
    """Converts audio from a given filepath into its equivalent text"""

    def __init__(self, api_key: str, region: str, filepath: str):
        super().__init__(api_key, region)
        self.filepath = filepath

    def run(self) -> str:
        audio_input = speechsdk.AudioConfig(filename=self.filepath)
        speech_recognizer = speechsdk.SpeechRecognizer(
            speech_config=self.speech_config, audio_config=audio_input)
        result = speech_recognizer.recognize_once_async().get()
        return result


class SpeechWordSegmentater(AzureSpeechUtils):
    """Splits audio from a given filepath into its constituent words and stores it in the output_path"""

    def __init__(self, api_key: str, region: str, filepath: str, output_path: str):
        super().__init__(api_key, region)
        self.filepath = filepath
        self.output_path = output_path

    def run(self) -> None:
        output_path = self.output_path
        filepath = self.filepath
        os.makedirs(output_path, exist_ok=True)
        audio = AudioSegment.from_wav(filepath)
        result = SpeechToText(self.api_key, self.region,
                              filepath=filepath).run()
        stt: Dict[str, Any] = json.loads(result.json)
        res: List[Dict[str, str]] = stt['NBest'][0]['Words']
        count = 1
        buffer = 200
        for word in res:
            text = word['Word']
            offset = word['Offset']
            duration = word['Duration']

            t1 = self.get_milliseconds(offset)
            t2 = t1 + self.get_milliseconds(duration) + buffer

            split_audio = audio[t1:t2]
            export_path = os.path.join(output_path, f'split{count}-{text}.wav')
            split_audio.export(export_path, format='wav')
            count += 1


#! INCOMPLETE
class PronunciationDetecter:
    """INCOMPLETE"""

    def __init__(self, text, audio, api_key, region):
        super().__init__()
        self.text = text
        self.audio = audio
        self.speech_to_text_model = SpeechToText(api_key, region, audio)
    
    def run(self) -> List[bool]:
        predicted_text = self.speech_to_text_model.run()
        return [True if pred_word == true_word else False for pred_word, true_word in zip(predicted_text, self.text)]


def main():
    load_dotenv()
    API_KEY = os.environ['API_KEY']
    REGION = os.environ['REGION']
    INPUT_PATH = 'D:\\Learn\python\\audiorecept\\pronunciation_test\\metro_V.wav'
    OUTPUT_PATH = "D:\\Learn\\python\\audiorecept\\split_segment\\"

    transcript = SpeechToText(API_KEY, REGION, INPUT_PATH).run()
    print(transcript.text)
    SpeechWordSegmentater(API_KEY, REGION, INPUT_PATH, OUTPUT_PATH).run()


if __name__ == '__main__':
    main()
