import json
import queue
import signal
from typing import Dict

import sounddevice as sd
import vosk
from channels.generic.websocket import WebsocketConsumer


class WSConsumer(WebsocketConsumer):

    def connect(self):
        self.accept()
        q: queue[bytes] = queue.Queue()

        def callback(indata, frames, time, status):

            q.put(bytes(indata))

        try:

            model = vosk.Model("model")
            results: Dict[str, str] = {}  # text from input
            with sd.RawInputStream(
                    samplerate=44100, blocksize=8000,
                    device=None, dtype='int16',
                    channels=1, callback=callback):

                rec = vosk.KaldiRecognizer(model, 44100)
                self.send(json.dumps({'message': "\n start speaking"}))
                self.send(json.dumps({'message': " "}))
                i = 0
                if i <= 5:
                    while True:
                        data = q.get()
                        if rec.AcceptWaveform(data):
                            results = json.loads(rec.Result())
                            self.send(json.dumps({'message': "\n\n" + results["text"]}))
                            results.clear()
                            i = i + 1
                        else:
                            # PUT WORD SEGMENTATION HERE
                            # Whatever results we get, split
                            # with open("gPartial.txt", "a") as f:
                            #     f.write(rec.PartialResult())
                            #     f.close()
                            pass
                else:
                    self.send(json.dumps({'message': "\n SESSION ENDED THNAKS"}))

        except KeyboardInterrupt:
            signal.CTRL_C_EVENT
