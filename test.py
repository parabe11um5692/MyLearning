""" from math import sqrt

critics_score = {
    "Анна": {"Книга1": 5, "Книга2": 3, "Книга3": 4},
    "Борис": {"Книга1": 2, "Книга2": 5, "Книга3": 1},
    "Виктор": {"Книга1": 4, "Книга2": 4, "Книга3": 5},
}

print('Эта программа высчитает, насколько два критика (Анна, Борис, Виктор) схожи в своих оценках, исходя из метрики косинусного сходства. Значение будет в пределах от -1 до 1, где 1 - полное сходство. Просто введите 2 имени и начнём!')

first_critic  = input('Введите имя первого критика: ')
second_critic = input('Введите имя второго критика: ')

if first_critic and second_critic in critics_score:
    if (first_critic == "Анна" and second_critic == "Борис") or (first_critic == "Борис" and second_critic == "Анна"):
        x1,y1,z1 = critics_score["Анна"]["Книга1"], critics_score["Анна"]['Книга2'], critics_score["Анна"]['Книга3']
        x2,y2,z2 = critics_score["Борис"]["Книга1"], critics_score["Борис"]['Книга2'], critics_score["Борис"]['Книга3']
    elif (first_critic == "Анна" and second_critic == "Виктор") or (first_critic == "Виктор" and second_critic == "Анна"):
        x1,y1,z1 = critics_score["Анна"]["Книга1"], critics_score["Анна"]['Книга2'], critics_score["Анна"]['Книга3']
        x2,y2,z2 = critics_score["Виктор"]["Книга1"], critics_score["Виктор"]['Книга2'], critics_score["Виктор"]['Книга3']
    elif (first_critic == "Борис" and second_critic == "Виктор") or (first_critic == "Виктор" and second_critic == "Борис"):
         x1,y1,z1 = critics_score["Борис"]["Книга1"], critics_score["Борис"]['Книга2'], critics_score["Борис"]['Книга3']
         x2,y2,z2 = critics_score["Виктор"]["Книга1"], critics_score["Виктор"]['Книга2'], critics_score["Виктор"]['Книга3']

    cos_sim = ((x1 * x2) + (y1 * y2) + (z1 * z2))/(sqrt(x1 ** 2 + y1 **2 + z1 **2) * sqrt(x2 **2 + y2 **2 + z2 ** 2))
    print(f"Результат вычислений: {round(cos_sim, 3)} или {cos_sim:.2%}")
else:
    print('Проверьте правильность введенных данных')
 """ 
""" 
print(f'Фильмы, которые посмотрели оба пользователя:  {", ".join(user1 & user2)}')
print(f'Фильмы, которые видел только user1: {", ".join(user1 - user2)}')
print(f'Фильмы, которые видел только user2:  {", ".join(user2 - user1)}')
print(f'Все фильмы, которые кто-то из них смотрел: {", ".join(user1 | user2)}')

recomend_for_user1 = (user1 | user2) - user1
recomend_for_user2 = (user1 | user2) - user2

print(f'Рекомендации для первого пользователя: {", ".join(recomend_for_user1)}')
print(f'Рекомендации для второго пользователя: {", ".join(recomend_for_user2)}') """


first_critic  = {"Книга1": 5, "Книга2": 3, "Книга3": 4}
second_critic = {"Книга1": 2, "Книга3": 5, "Книга4": 1}
third_critic  = {"Книга1": 4, "Книга2": 4, "Книга3": 5}

critics_score = [first_critic, second_critic, third_critic]

common = critics_score[0].keys()

for critic in critics_score[1:]:
    common &= critic.keys()

list_of_common_scores = [] #вытягиваем оценки для общих книг от каждого критика

for book in common:
    ratings = []
    for elem in critics_score:
        ratings.append(elem.get(book))
    list_of_common_scores.append(ratings)

list_of_abs_deviations = [] #высчитываем отклонения 
for scores in list_of_common_scores:
    mean_value = sum(scores) / len(scores)
    abs_devs = [abs(score - mean_value) for score in scores]  # модуль отклонений
    list_of_abs_deviations.append(sum(abs_devs) / len(abs_devs))  # среднее отклонение для книги

MAD = round(sum(list_of_abs_deviations) / len(list_of_abs_deviations), 2)
print(MAD)
