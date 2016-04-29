# -*- coding: utf-8 -*-


alphabet = 'abcdefghijklmnopqrstuvwxyz'


# функция шифрует и дешефрует текст на указанное смещение
def encoding(text, shift):
    encoding_text = []
    alpha_len = len(alphabet)
    for x in text:
        if x in alphabet:
            encoding_text.append(alphabet[
                (alphabet.index(x)+int(shift)) % alpha_len])
        else:
            encoding_text.append(x)
    encoding_text = ''.join(encoding_text)
    return {'result': encoding_text}


def letter_count(text):
    count_letters = {}   # Счетчик символов из алфавита
    count_all = {}  # Счетчик всех символов для отображения в диаграмме
    for x in set(text):
        if x != ' ':
            count_all.update({x: text.count(x)})
        if x in alphabet:
            count_letters.update({x: text.count(x)})
        else:
            continue
    len_text = len(text)
    max_hit_shift = crack_shift(count_letters, len_text)
    if max_hit_shift == 0:
        max_hit_shift = 'Текст не зашифрован'
    return {'result_count': count_letters,
            'max_hit_shift': max_hit_shift,
            'result_count_all': count_all}


# Функция вычисления приблизительного сдвига путем частотного анализа
def crack_shift(count_letters, len_text):
    # Частота использования букв  в англ. языке
    weight = (6.51, 1.89, 3.06, 5.08, 17.4,
              1.66, 3.01, 4.76, 7.55, 0.27,
              1.21, 3.44, 2.53, 9.78, 2.51,
              0.29, 0.02, 7.00, 7.27, 6.15,
              4.35, 0.67, 1.89, 0.03, 0.04, 1.13)

    text_weight = [0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0, 0]
    # Заполнение списка частоты использования букв в тексте
    for num, x in enumerate(alphabet):
        if x in count_letters:
            text_weight[num] = round(100.0 / len_text*count_letters[x], 2)
        else:
            continue
    return found_shift(weight, text_weight)


# Вычисление сдвига с наибольшим количеством совпадений
# исходного кортежа с списком частоты использования в тексте
def found_shift(weight, text_weight):
    max_hit = 0
    max_hit_shift = 0
    for num_alphabet in range(len(alphabet)):  # Имитация сдвига
        hit_count = 0
        for num_letter in range(len(alphabet)):  # Обход словаря
            if (num_letter+num_alphabet) >= len(alphabet):
                num_shift = (num_letter+num_alphabet) - len(alphabet)
            else:
                num_shift = (num_letter+num_alphabet)
            # Сравнение исходной частоты использования англ. букв с частотой
            # использования в тексте введенным пользователем с сдвигом
            # num_shift
            if int(weight[num_letter]) == int(text_weight[num_shift]):
                hit_count += 1

                if max_hit < hit_count:
                    max_hit = hit_count
                    max_hit_shift = num_alphabet
    return max_hit_shift


def is_valid_request(*args):
    return is_empty_request(args) and is_numb_shift(args[1])


def is_empty_request(args):
    return '' not in args


def is_numb_shift(shift):
    try:
        int(shift)
    except ValueError:
        return False
    return True
