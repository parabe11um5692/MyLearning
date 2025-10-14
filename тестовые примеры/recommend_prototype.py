"""Эта программа - прототип рекомендательной системы. Вводим оценки для 6 фильмов, программа находит пользователя с наиболее схожими оценками и, 
если у него есть фильмы, которые вы не видели, советует их к просмотру"""

import numpy as np
import re

user1 = [2, 4, 3, 0, 2, 1]
user2 = [0, 0, 1, 4, 3, 5]
user3 = [2, 1, 4, 5, 5, 5]
user4 = [0, 1, 2, 5, 1, 4]

movies = {
    0: "Матрица",
    1: "Интерстеллар",
    2: "Джентльмены",
    3: "Начало",
    4: "Дюна",
    5: "Темный рыцарь"
}

try:
    #ловим данные от пользователя и создаем возможность вводить через запятую или пробел
    user_input =  input('Введите целочисленные оценки для 6 фильмов:')
    numbers = [int(x) for x in re.findall(r'\d+', user_input)]
    #формируем массив на основе полученных данных
    user = np.array(numbers, dtype='int8')
    #остальных критиков записываем в матрицу
    user_scores_matrix = np.array([(user1),(user2),(user3),(user4)])

    def calc_cos_dist(user_1_as_array: list, user_2_as_array: list):
        """Возвращает косинусное расстояние между двумя пользователями """
        dot_multiply = np.dot(user_1_as_array, user_2_as_array)#числитель
        user_v_norm = np.linalg.norm(user_1_as_array)#первый множитель из знаменателя
        user_from_matrix_v_norm = np.linalg.norm(user_2_as_array)#второй множитель из знаменателя
        similarity = dot_multiply / (user_v_norm * user_from_matrix_v_norm)#получаем сходство
        distance = 1 - similarity#находим расстояние
        return distance

    distances = np.array([calc_cos_dist(user, elem) for elem in user_scores_matrix])#формируем массив для каждого пользователя в сравнении с нашим user'ом

    best_user_index = np.argmin(distances)#находим индекс лучшего попадания
    best_user = user_scores_matrix[best_user_index]#находим оценки лучшего попадания

    print(f'Пользователь {best_user_index + 1} имеет с вами наименьшее расстояние в {distances[best_user_index]:.3f}')

    found_rec_film = False #заглушка для получения фильмов, которые не видел user, но видел ближайший к нему пользователь

    for i, rating in enumerate(user):
    #пробегаемся по нумерованной версии оценок пользователя и сопоставляем оценки с названиями фильмов
        if rating == 0 and best_user[i] > 0:
            print(f'Посмотрите фильм "{movies[i]}"')
            found_rec_film = True#если есть фильм, который наш пользователь не видел - меняем заглушку
    if not found_rec_film:
            print(f'Между вами и Пользователем {best_user_index + 1} нет разных фильмов')

except Exception as ex:
     print('Проверьте правильность введенных данных!')
     print('\n')
     print(ex)

