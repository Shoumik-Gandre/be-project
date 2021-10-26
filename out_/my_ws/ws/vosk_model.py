class VoskModel:
    pass


"""
Accept waveforms
get input in wav file object -> vosk functions that accept wav.
input through django is VERY SPECIFIC FORMAT
make sure varun tests give you false

wf-wav object
mono PCM format
if wf.getnchannels() != 1 or wf.getsampwidth() != 2 or wf.getcomptype() != "NONE":
    print ("Audio file must be WAV format mono PCM.")
"""
