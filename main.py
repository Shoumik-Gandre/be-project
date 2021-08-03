import time

from allosaurus.app import read_recognizer
from allosaurus.lm.inventory import Inventory
from allosaurus.model import get_model_path


def main():
    model_name = 'eng2102'
    # load your model
    model = read_recognizer()
    # model_path = get_model_path('latest')
    # inventory = Inventory(model_path)
    #
    # print("Available Languages")
    # for lang_id, glotto_id, lang_name in zip(inventory.lang_ids, inventory.glotto_ids, inventory.lang_names):
    #     lang_name = lang_name.encode('ascii', 'ignore')
    #     if lang_name == b'english':
    #         print('- ISO639-3: ', lang_id, 'Glotto Code', glotto_id, ' name: ', lang_name)

    # run inference -> æ l u s ɔ ɹ s
    start = time.perf_counter_ns()
    phonemes = model.recognize('sample2.wav', lang_id='eng')
    stop = time.perf_counter_ns()
    print(f"time taken = {stop - start}")
    print(phonemes)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

