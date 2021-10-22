import vosk
from django.apps import AppConfig
from django.conf import settings


class JaishrutiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'jaishruti'
    vosk_model = vosk.Model(settings.VOSK_MODEL_PATH)
    vosk_asr = vosk.KaldiRecognizer(vosk_model, 44100)
