import json
from random import randint
from time import sleep
from channels.generic.websocket import WebsocketConsumer


def read_file():
    output = []
    # for i in range(1000):
    file1 = open(r'C:\Users\ganes\vosk-api-master\python\example\gaja.txt', 'r')
    Lines = file1.readlines()
    for line in Lines:
        output.append(line)
    return output


class WSConsumer(WebsocketConsumer):

    def connect(self):
        self.accept()
        # for i in range(1000):
        output = []
        k = 0
        j = 0
        for i in range(1000):
            file1 = open(r'C:\Users\ganes\vosk-api-master\python\example\gaja.txt', 'r')
            Lines = file1.readlines()
            for line in Lines:
                output.append(line)
                if k <= j:
                    self.send(json.dumps({'message': output[j]}))
                    j = j + 1
            k = j
            j = 0
            sleep(10)
