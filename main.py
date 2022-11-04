import numpy as np


def fit(input_txt):
    # считываем текст
    try:
        with open(input_txt, 'r', encoding='utf-8') as file:
            text = file.read()

        # разбиваем текст на отдельные слова, сохранив при этом знаки препинания ->
        # -> чтобы сгенерированный текст был со знаками препинания
        splited_text = text.split()
        return splited_text
    except FileNotFoundError:
        return list()


# функция-генератор, создающая пары слов
def make_pairs(splited_txt):
    # перебираем все слова в подготовленном тексте, кроме последнего
    for i in range(len(splited_txt) - 1):
        # генерируем новую пару и возвращаем её как результат работы функции
        yield (splited_txt[i], splited_txt[i + 1])


def generate(splited_txt, lenght):
    # вызываем генератор и получаем все пары слов
    pairs = make_pairs(splited_txt)

    # словарь, который будет содержать слова и их продолжения ->
    # -> в качестве ключа - слово, в качестве значения - список возможных продолжений
    word_dict = {}

    # перебираем все пары слов из списка пар
    for word_1, word_2 in pairs:
        # если первое слово уже было добавлено в словарь
        if word_1 in word_dict.keys():
            # тогда второе слово добавим как возможное продолжение первого
            word_dict[word_1].append(word_2)
        else:
            # если первого слова ещё не было в словаре, ->
            # -> создаём новую запись в словаре и указываем второе слово как продолжение первого
            word_dict[word_1] = [word_2]

    # выбираем первое слово(случайно) для генерации новой последовательности
    first_word = np.random.choice(splited_txt)

    # Для красоты вывода, мы хотим начинать нашу новую последовательность с большой буквы ->
    # -> поэтому если в нашем первом слове нет заглавных букв, то будем искать до тех пор, пока не найдём
    while first_word.islower():
        first_word = np.random.choice(splited_txt)

    # новая последовательность
    sequence = [first_word]

    # количество слов в новой последовательности
    number_of_words = lenght

    # цикл заполняющий последовательность
    for i in range(number_of_words):
        # на каждой итерации добавляем одно из прололжений для слова - случайно
        sequence.append(np.random.choice(word_dict[sequence[-1]]))

    result = ' '.join(sequence)
    print(result)
    # выводим нашу последовательность в файл generated.txt
    with open('generated.txt', 'w') as file2:
        file2.write(' '.join(sequence))


# блок, обрабатывающий ввод и запускающий обучение, а затем и генерацию
def main():
    input_txt = input("Введите полное название текстового файла вместе с расширением: ")
    sp_txt = fit(input_txt)
    if '.txt' not in input_txt:
        print("Было введено некорректное значение файла. Попробуйте еще раз.")
        main()
    elif not sp_txt:
        print("К сожалению, файла с таким именем не существует. Попробуйте еще раз.")
        main()
    else:
        length = int(input("Введите число слов, которое должно быть в сгенерированной последовательности: "))
        generate(sp_txt, length)


if __name__ == '__main__':
    main()
