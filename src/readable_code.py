import pathlib
import sys


ROOT_DIR = pathlib.Path('./../')
DATA_DIR = ROOT_DIR / 'data'

DICTIONARY_DATA = 'dictionary-data.txt'
DICTIONARY_DATA_PATH = DATA_DIR / DICTIONARY_DATA


def main():

    # 実行時引数を取得
    args = sys.argv

    # 表示するIDを取得
    dict_id = None
    if len(args) > 0:
        dict_id = args[0]


    # 読み込んだ辞書データ格納用
    dic_data = dict()

    # ファイル読み込み
    with open(DICTIONARY_DATA_PATH, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        for i, word in enumerate(lines):
            dic_data[i] = word.strip()
            # print(f'{i}: {word.strip()}')

    # 辞書の表示
    if dict_id is None:
        pass
        # TODO: 全ての辞書を表示
    else:
        pass
        # TODO: dict_idで指定されたものを表示


if __name__ == '__main__':
    main()
