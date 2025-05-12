from math import sqrt

#вложенный словарь с критиками и их оценками для фильмов
critics_score = {
    'Лиза Роуз' : {
        'Девушка из воды' : 2.5,
        'Змеиный полёт' : 3.5,
        'Поцелуй на удачу': 3.0,
        'Супермен: Возвращение' : 3.5,
        'Ты, Я и Дюпри' : 2.5,
        'Ночной слушатель' : 3.0
    },

    'Майкл Филлипс' : {
        'Девушка из воды' : 2.5,
        'Змеиный полёт' : 5.0,
        'Супермен: Возвращение' : 1.5,
        'Ночной слушатель' : 4.0
    },

    'Клаудия Пик' : {
        'Змеиный полёт' : 3.5,
        'Поцелуй на удачу': 3.0,
        'Ночной слушатель' : 4.5,
        'Супермен: Возвращение' : 4.0,
        'Ты, Я и Дюпри' : 2.5,
    },

    'Мик Ласель' : {
        'Девушка из воды' : 3.0,
        'Змеиный полёт' : 4.0,
        'Поцелуй на удачу': 2.0,
        'Супермен: Возвращение' : 3.0,
        'Ночной слушатель' : 3.0,
        'Ты, Я и Дюпри' : 2.0,
    },

    'Джек Метьюз' : {
        'Девушка из воды' : 3.0,
        'Змеиный полёт' : 5.0,
        'Ночной слушатель' : 3.0,
        'Супермен: Возвращение' : 5.0,
        'Ты, Я и Дюпри' : 4,
    },

    'Ген Сеймур' : {
        'Девушка из воды' : 3.0,
        'Змеиный полёт' : 3.5,
        'Поцелуй на удачу': 1.5,
        'Супермен: Возвращение' : 5.0,
        'Ты, Я и Дюпри' : 3.5,
        'Ночной слушатель' : 3.0
    },


    'Я' : {
        'Змеиный полёт' : 3.0,
        'Ты, Я и Дюпри' : 2.5,
        'Супермен: Возвращение' : 4.0,
    },
}

def evklid_distance(data_score, person_1, person_2):
    """Функция возвращает обратное Евклидово расстояние для двух критиков, оцененных по набору данных, где 1 - максимальная схожесть, 0 - абсолютная разница"""

    #создадим словарь, куда попадут только те фильмы, которые оценивали оба критика
    score_for_both_persons = {}

    #переберем значения, которые есть для двух критиков и которые не равны 0. если есть хотя бы одно такое - продолжаем работу
    for item in data_score[person_1]:
        if item in data_score[person_2] and data_score[person_1][item] != 0 and data_score[person_2][item] != 0:
            score_for_both_persons[item] = 1
    #создадим условие на случай отсутствия одинаковых фильмов для оценки
    if len(score_for_both_persons) == 0:
        return f"У критиков {person_1} и {person_2} нет общих фильмов для оценивания"
    #проведем рассчеты по формуле Евклидового расстояния и генератором из последовательности фильмов, оцененных двумя критиками
    evklid_summ_of_squares = sum([pow(data_score[person_1][item] - data_score[person_2][item], 2) 
                                  for item in score_for_both_persons])
    #извлекаем корень, инвертируем результат и выводим
    evklid_dist = sqrt(evklid_summ_of_squares)
    result = round(1/(1 + evklid_dist), 3)

    # Изменить логику интерпретации
    if result < 0.5:
        return result
    elif result >= 0.5:
        return result

# Вывод результата

def pirson_ratio(data_score, person_1, person_2):
    """Расчет схожести оценки фильмов для двух пользователей на основе переданного словаря с оценками. Оценка 1 - максимальная схожесть, оценка -1 - полное различие"""
    score_for_both_persons = {}

    for item in data_score[person_1]:
        if item in data_score[person_2] and data_score[person_1][item] != 0 and data_score[person_2][item] != 0:
            score_for_both_persons[item] = 1
    
    num_of_intersections = len(score_for_both_persons)

    if num_of_intersections == 0:
        return f'У критиков {person_1} и {person_2} нет общих фильмов. Расчет невозможен!'

    sum_of_first_user_scores  =  sum([data_score[person_1][item] for item in score_for_both_persons])
    sum_of_second_user_scores =  sum([data_score[person_2][item] for item in score_for_both_persons])

    squared_sum_of_first_user  = sum([pow(data_score[person_1][item], 2) for item in score_for_both_persons])
    squared_sum_of_second_user = sum([pow(data_score[person_2][item], 2) for item in score_for_both_persons])

    sum_of_multipl = sum([data_score[person_1][item] * data_score[person_2][item] for item in score_for_both_persons])

    pirson_calc_numerator = sum_of_multipl - (sum_of_first_user_scores * sum_of_second_user_scores / num_of_intersections)
    pirson_calc_denominator = sqrt((squared_sum_of_first_user  - pow(sum_of_first_user_scores, 2) / num_of_intersections) *
                              (squared_sum_of_second_user - pow(sum_of_second_user_scores, 2) / num_of_intersections))
    
    if pirson_calc_denominator == 0:
        return 'Произведение отклонений равно 0, расчет невозможен'

    result = round(pirson_calc_numerator/pirson_calc_denominator,3)

    if result >= 0.5:
        res_of_comparison = 'Критики похожи'
    if result <= 0.5:
        res_of_comparison = 'Критики не похожи'
    return result

def best_critics(data_score, person, num_of_critics = 5, calc_method = evklid_distance):
    """Функция для поиска наилучшего критика путем перебора всех критиков и сопоставления их оценок с оценками пользователя. Можно выбирать между несколькими способами расчетов"""
    scores = [(calc_method(data_score, person, other), other)
              for other in data_score if other != person]#генерируем список из всех критиков, перебирая их указанным методом
    
    scores.sort(reverse = True) #разворачивам список для получения одного лучшего критика

    if calc_method == evklid_distance:
        return f'Лучший критик для вас по Евклидову расстоянию это: {scores[0][1]}, ваше соотношение равно {scores[0][0]}'
    if calc_method == pirson_ratio:
        return f'Лучший критик для вас по коэффициенту Пирсона это: {scores[0][1]}, ваше соотношение равно {scores[0][0]}'
    #вывод лучшего критика в зависимости от выбранного метода расчетов
print(best_critics(critics_score, "Я"))
print(best_critics(critics_score, "Я", calc_method= pirson_ratio))
