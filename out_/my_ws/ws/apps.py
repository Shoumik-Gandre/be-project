import vosk
from django.apps import AppConfig
from django.conf import settings


class WsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'ws'
    vosk_model = ''#vosk.Model(settings.VOSK_MODEL_PATH)
    vosk_asr = ''#vosk.KaldiRecognizer(vosk_model, 44100) # access through vosk model
