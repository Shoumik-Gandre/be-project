import json

from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import render
import wave
from django.views.decorators.csrf import csrf_exempt
from . import apps
from .models import Sentence
from .word_comparater import compare_sentence


def index(request: HttpRequest):
    return render(request, 'recorder/record.html', context={
        'sentences': Sentence.objects.all()
    })


@csrf_exempt
def upload(request: HttpRequest):
    if request.method == 'POST':
        filename = request.POST['fname']
        sound_file = request.FILES['data']
        sound_file = wave.open(sound_file, 'rb')
        apps.RecorderConfig.vosk_asr.SetWords(True)
        apps.RecorderConfig.vosk_asr.AcceptWaveform(sound_file.readframes(sound_file.getnframes()))
        result = json.loads(apps.RecorderConfig.vosk_asr.FinalResult())
        sentence_id = request.POST.get('sentence_id', None)
        result['sentence_id'] = sentence_id
        sentence = Sentence.objects.get(pk=int(sentence_id))
        print(result)

        ### COMPARE sentence AND result['text'] here
        mask = compare_sentence(sentence.text, result['text'])
        print(mask)
        result['mask'] = mask
    return JsonResponse(json.dumps(result), safe=False)
