import pathlib
import sys


ROOT_DIR = pathlib.Path('./../')
DATA_DIR = ROOT_DIR / 'data'

DICTIONARY_DATA_PATH = [DATA_DIR / 'dictionary-data.txt']
USER_DATA_LIST = ['kou']



def print_dict_data(dict_data, dict_id):
    """
    辞書内の単語情報表示
    辞書の中から指定されたIDの単語情報を表示する
    引数：
        dict_data: 単語情報が格納された辞書
        dict_id: 表示する単語情報のID
    注意：
        指定されたIDが辞書に格納されていることを呼び出し前に確認すること
    """
    print(f"{dict_id}: {dict_data[dict_id][0]} {dict_data[dict_id][1]}")


def read_dict_data(dict_data, dict_id_list, start_id, data_path):
    """
    入力ファイルから単語情報読み込み
    引数：
        dict_data: 単語情報を格納する辞書
        dict_id_list: 単語IDを格納するリスト
        start_id: IDの始まり番号
        data_path: 入力ファイルパス
    """
    # ファイル読み込み
    with open(data_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        for i, word in enumerate(lines):
            # IDを作成し、単語情報を格納する辞書とIDのリストに格納
            id = i + start_id
            dict_data[id] = word.strip().split(' ')
            dict_id_list.append(id)


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

    # 単語情報をファイルから読み込む
    read_dict_data(dict_data, dict_id_list, 1, DICTIONARY_DATA_PATH[0])

    # 辞書の表示
    if dict_id is None:
        # 全ての辞書を表示
        print(f"ユーザー名: {USER_DATA_LIST[0]}")
        for id in dict_id_list:
            print_dict_data(dict_data, id)
    else:
        # dict_idで指定されたものを表示
        if dict_id in dict_id_list:
            # 指定されたIDが存在する場合はそのIDの単語情報を表示
            print(f"ユーザー名: {USER_DATA_LIST[0]}")
            print_dict_data(dict_data, dict_id)
        else:
            # 指定されたIDが存在しない場合はメッセージを表示
            print("指定されたIDは存在しません")


if __name__ == '__main__':
    output_dictionary_data()
