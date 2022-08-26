def create_files():
    """Создаёт два файла."""
    with open("English.txt", "w"):
        pass
    with open("Russian.txt", "w"):
        pass


def append_ru_word(ru_words):
    """Добавляет русский перевод слова."""
    ru_words.append(ru_words[-1])


def delete_ru_word(ru_words):
    """Удаляет русский перевод слова."""
    del ru_words[-1]


def read_main_file():
    """Парсит главный файл и подготавливает данные к записи."""
    with open('PythonTest.txt', encoding='utf-8') as f:
        lines = f.readlines()[33:]
        for line in lines:
            words = line.split('\t')
            words[-1] = words[-1].replace('\n', '')
            if ';' in line:
                en_words = words[0].split(' ; ')
                ru_words = words[-1].split(' ; ')
                while len(en_words) < len(ru_words):
                    delete_ru_word(ru_words)
                while len(en_words) > len(ru_words):
                    append_ru_word(ru_words)
                append_ru_to_file(ru_words)
                append_en_to_file(en_words)
            elif ';' not in line:
                append_two_element(words)


def append_two_element(words):
    """Записывает данные в файл если words состоит из 2 элементов."""
    with open("Russian.txt", "a", encoding='utf-8') as f:
        f.write(words[-1] + '\n')
    with open("English.txt", "a", encoding='utf-8') as f:
        f.write(words[0] + '\n')


def append_ru_to_file(ru_words):
    """Записывает оставшиеся русские слова в файл."""
    with open("Russian.txt", "a", encoding='utf-8') as f:
        for ru_word in ru_words:
            f.write(ru_word + '\n')


def append_en_to_file(en_words):
    """Записывает оставшиеся английские слова в файл."""
    with open("English.txt", "a", encoding='utf-8') as f:
        for en_word in en_words:
            f.write(en_word + '\n')


def main():
    create_files()
    read_main_file()


if __name__ == '__main__':
    main()
