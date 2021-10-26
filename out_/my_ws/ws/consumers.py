import json
from queue import Queue
from collections import deque
import signal
from typing import Dict, Deque

import sounddevice as sd
from channels.generic.websocket import WebsocketConsumer
from .apps import WsConfig


class WSConsumer(WebsocketConsumer):

    def connect(self):
        self.accept()
        q: Queue[bytes] = Queue()
        data_store: Deque[bytes] = deque()

        def callback(in_data, frames, time, status):
            q.put(bytes(in_data))

        try:
            with sd.RawInputStream(
                    samplerate=44100, blocksize=8000,
                    device=None, dtype='int16',
                    channels=1, callback=callback):

                self.send(json.dumps({'message': "\n start speaking"}))
                self.send(json.dumps({'message': " "}))
                i = 0
                if i <= 5:
                    while True:
                        data = q.get()
                        data_store.append(data)
                        if WsConfig.vosk_asr.AcceptWaveform(data):
                            results: Dict[str, str] = json.loads(WsConfig.vosk_asr.Result())
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
                    self.send(json.dumps({'message': "SESSION ENDED"}))

        except KeyboardInterrupt:
            signal.CTRL_C_EVENT
