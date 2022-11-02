def main():
    input_file_path = './data/dictionary-data.txt'

    with open(input_file_path, 'r', encoding='utf-8') as f:
        s = f.read()
        print(s)


if __name__ == '__main__':
    main()
