import pathlib


ROOT_DIR = pathlib.Path('./../')
DATA_DIR = ROOT_DIR / 'data'

DICTIONARY_DATA = 'dictionary-data.txt'


def main():
    input_file_path = DATA_DIR / DICTIONARY_DATA

    with open(input_file_path, 'r', encoding='utf-8') as f:
        s = f.read()
        print(s)


if __name__ == '__main__':
    main()
