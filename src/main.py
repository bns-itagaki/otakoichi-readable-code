import pathlib
import sys


ROOT_DIR = pathlib.Path('./../')
DATA_DIR = ROOT_DIR / 'data'

DICTIONARY_DATA = 'dictionary-data.txt'
DICTIONARY_DATA_PATH = DATA_DIR / DICTIONARY_DATA


def output_dictionary_data():
    """
    単語情報表示処理
    入力ファイルから単語情報を読み込んで画面に表示する
    """

    # 実行時引数を取得
    args = sys.argv
    
    # 表示するIDを取得
    dict_id = None
    if len(args) > 1:
        dict_id = int(args[1])
    
    # 読み込んだ辞書データ格納用(辞書本体とIDのリスト)
    dict_data = dict()
    dict_id_list = []

    # ファイル読み込み
    with open(DICTIONARY_DATA_PATH, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        for i, word in enumerate(lines):
            # IDを作成し、単語情報を格納する辞書とIDのリストに格納
            id = i + 1
            dict_data[id] = word.strip().split(' ')
            dict_id_list.append(id)

    # 辞書の表示
    if dict_id is None:
        # 全ての辞書を表示
        for id in dict_id_list:
            print(f"{id}: {dict_data[id][0]}")
    else:
        # dict_idで指定されたものを表示
        if dict_id in dict_id_list:
            # 指定されたIDが存在する場合はそのIDの単語情報を表示
            print(f"{dict_id}: {dict_data[dict_id][0]}")
        else:
            # 指定されたIDが存在しない場合はメッセージを表示
            print("指定されたIDは存在しません")


if __name__ == '__main__':
    output_dictionary_data()
