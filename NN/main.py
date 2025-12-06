import numpy as np

def activate(x):
    """Активирующая функця. Возвращает гиперболический тангенс"""
    return np.tanh(x)

def derivative(y):
    "Возвращает производную от итогового значения"
    return 1 - y**2

#формируем веса для входного и скрытого слоя
first_layer  = np.array([[-0.2, 0.3, -0.4],
                         [0.1, -0.3, -0.4]])

second_layer = np.array([0.2, 0.3])

def go(data):
    """Запуск НС"""

    weighted_sum_hidden = np.dot(first_layer, data)#высчитыавем взвешенную сумму весов для скрытого слоя
    intermid_res = activate(weighted_sum_hidden)#пытаемся запустить нейрон, опираясь на его взвешенную сумму

    weighted_sum_output = np.dot(second_layer, intermid_res)#высчитываем выходную взвешенную сумму 
    final_res = activate(weighted_sum_output)#получаем y, опираясь на выходную взвешенную сумму

    return final_res, intermid_res

def train(data_set, lr=0.01, num_of_attempts=10000): #передаем набор данных, шаг для корректировки и кол-во повторений
    """Запускает обучение НС"""
    global first_layer, second_layer

    count = len(data_set)

    for _ in range(num_of_attempts):
        x = np.array(data_set[np.random.randint(0, count)])
        input_data = x[0:3]
        target = x[-1]

        # Прямой проход
        final_res, intermid_res = go(input_data)

        # Ошибка на выходном нейроне
        error = final_res - target
        local_gradient_output = error * derivative(final_res)

        # Обновление весов второго слоя
        second_layer -= lr * local_gradient_output * intermid_res

        # Градиенты для первого слоя
        local_gradient_hidden = second_layer * local_gradient_output * derivative(intermid_res)

        # Обновление весов первого слоя
        first_layer[0, :] -= lr * local_gradient_hidden[0] * input_data
        first_layer[1, :] -= lr * local_gradient_hidden[1] * input_data

data_set = [(-1, -1, -1, -1),
         (-1, -1, 1, 1),
         (-1, 1, -1, -1),
         (-1, 1, 1, 1),
         (1, -1, -1, -1),
         (1, -1, 1, 1),
         (1, 1, -1, -1),
         (1, 1, 1, -1)]


train(data_set)

for x in data_set:
    final_res, _ = go(x[0:3])
    print(f'Результат работы: {final_res:.3f} => {x[-1]}')
