from pprint import pprint

with open('phone.txt', 'r', encoding='utf-8') as phonefile:
    text = phonefile.read()

mat = [x.split('\t')[1:3] for x in text.split('\n')]
phoneme_conv = {x[0]: x[1] for x in mat}
pprint(phoneme_conv, indent=4)
print(len(phoneme_conv.values()))
