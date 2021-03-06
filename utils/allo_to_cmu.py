allo_to_cmu = {
    'aɪ': 'AY',
    'aʊ': 'AW',
    'b': 'B',
    'd': 'D',
    'dʒ': 'JH',
    'eɪ': 'EY',
    'f': 'F',
    'h': 'HH',
    'i': 'IY',
    'j': 'Y',
    'k': 'K',
    'l': 'L',
    'l̩': 'EL',
    'm': 'M',
    'm̩': 'EM',
    'n': 'N',
    'n̩': 'EN',
    'oʊ': 'OW',
    'p': 'P',
    's': 'S',
    't': 'T',
    'tʃ': 'CH',
    'u': 'UW',
    'v': 'V',
    'w': 'W',
    'z': 'Z',
    'æ': 'AE',
    'ð': 'DH',
    'ŋ': 'NG',
    'ɑ': 'AA',
    'ɔ': 'AO',
    'ɔɪ': 'OY',
    'ə': 'AX',
    'ɚ': 'AXR',
    'ɛ': 'EH',
    'ɝ': 'ER',
    'ɡ': 'G',
    'ɨ': 'IX',
    'ɪ': 'IH',
    'ɹ': 'R',
    'ɾ': 'DX',
    'ɾ̃': 'NX',
    'ʃ': 'SH',
    'ʉ': 'UX',
    'ʊ': 'UH',
    'ʌ': 'AH',
    'ʍ': 'WH',
    'ʒ': 'ZH',
    'ʔ': 'Q',
    'θ': 'TH'
}

if __name__ == '__main__':
    print([allo_to_cmu.get(x, "[N/A]") for x in input("Enter ascii phonemes: ").split(' ') if x != '.'])
