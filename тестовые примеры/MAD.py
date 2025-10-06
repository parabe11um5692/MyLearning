#Эта программа высчитывает метрику MAD(среднее абсолютное отклонение) для любого числа критиков

first_critic  = {"Книга1": 5, "Книга2": 3, "Книга3": 4}
second_critic = {"Книга1": 2, "Книга3": 5, "Книга4": 1}
third_critic  = {"Книга1": 4, "Книга2": 4, "Книга3": 2}

critics_score = [first_critic, second_critic, third_critic]

#берем оценки первого критика за стартовое множество, с которым будем сравнивать всех последующих критиков
common = critics_score[0].keys()

for critic in critics_score[1:]:
    common &= critic.keys()

list_of_common_scores = [] #вытягиваем оценки для общих книг от каждого критика

for book in common: 
    #необходимо создание двух кортежей, чтобы оценки рассматривались в рамках той книги, 
    # для которой они были выставлены, в противном случае начинаются ошибки в вычислениях
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
print(f'Среднее абсолютное отклонение (MAD) составляет {MAD}')


# В процессе работы была изучена специфика формулы MAD, сама формула разобрана на составные части и применена к поставленной задаче. 
# Первая версия кода не отличалась масштабируемостью и гибкостью, имелась строгая зависимость работы от числа критиков. Переписал. Теперь всё работает и для 3 и для 23 критиков. \
# Возможно, следует нанизать код на Numpy, дабы повысить масштабируемость и обеспечить корректную работу с экстремально большими выборками. Но для тестового примера - пойдет.