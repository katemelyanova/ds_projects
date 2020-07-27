import numpy as np
number = np.random.randint(1, 101)


def game_core(number):
    '''
    Для отгадывания числа используется метод бинарного поиска. Определяется нижняя и верхняя
    границы заданного интервала, середина которого - предполагаемое число. Переносятся границы
    интервала, сокращая область поиска, находится загаданное число.
    Функция принимает заданное число и возвращает число попыток его угадывания
    '''
    count = 1
    lower_border = 0
    upper_border = 100
    guess_number = round((lower_border+upper_border) / 2)

    while True:
        if guess_number == number:
            break
        elif guess_number < number:
            lower_border = guess_number  # нижней границей становится середина интервала
            # из прошлого шага цикла
            guess_number = round((lower_border+upper_border) / 2)  # определяется новая середина
            # интервала - предполагаемое заданное число
        else:  # if guessed_number > number
            upper_border = guess_number  # верхней границей становится середина интервала
            # из прошлого шага цикла
            guess_number = round((lower_border+upper_border) / 2)  # определяется новая середина
            # интервала - предполагаемое заданное число
        count += 1
    return count  # выход из цикла, если найдено загаданное число


def score_game(game_score):
    '''
    Игра запускается 1000 раз для определения скорости угадываения заданного числа
    Функция принимает результат выполнения фунцкии game_score и сообщает, за сколько попыток
    алгоритм в среднем угадывает число
    '''
    count_list = []
    np.random.seed(1)  # фиксирование random seed для воспроизводимости эксперимента
    random_array = np.random.randint(1, 101, size=1000)
    for num in random_array:
        count_list.append(game_core(number))
    score = int(np.mean(count_list))  # среднее кол-во попыток угадывания (тысяча экспериментов)
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return score


score_game(game_core)
