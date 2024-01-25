import matplotlib
import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt

# Установка бэкенда TkAgg для корректной работы с PyInstaller
matplotlib.use('TkAgg')
print('Введите эмпирические координаты кривой (Ваш ряд расходов воды в м3/с):')
def input_water_expenses(prompt):
    print(prompt)
    values = []
    while True:
        value = input()
        if not value:
            break
        values.append(float(value))
    return np.array(values)

# Ввод первого массива
empiric_array = input_water_expenses("Введите эмпирические координаты кривой (Ваш ряд расходов воды в м3/с):\n")

# Ввод второго массива
analytic_array = input_water_expenses("Введите аналитические координаты кривой () ряд расходов воды в м3/с:\n")

emp_coord = np.arange(1,len(empiric_array)+1)
emp_coord_to_1 = emp_coord / (len(empiric_array) +1)
# Задайте среднее и стандартное отклонение
mean = 0  # Среднее значение
std_dev = 1  # Стандартное отклонение
x_empiric = norm.ppf(emp_coord_to_1, loc=mean, scale=std_dev)


# РИСУЕМ КРИВУЮ ОБЕСПЕЧЕННОСТЕЙ КРИЦКОГО-МЕНКЕЛЯ:
x_coord = np.array([-3.719016485, -3.090232306, -2.747781385, -2.575829304, -2.326347874, -1.880793608, -1.644853627, -1.281551566, -0.841621234, -0.67448975, -0.524400513, -0.253347103, 0, 0.253347103, 0.524400513, 0.67448975, 0.841621234, 1.281551566, 1.644853627, 1.880793608, 2.326347874, 2.575829304, 2.747781385, 3.090232306])
y_coord = analytic_array

xticks_combined = [0.01, 0.1, 0.3, 0.5, 1, 3, 5, 10, 20, 25, 30, 40, 50, 60, 70, 75, 80, 90, 95, 97, 99, 99.5, 99.7, 99.9]

plt.figure(figsize=(10, 6))
plt.scatter(x_empiric,np.sort(empiric_array)[::-1], label="Эмпирическая",s=8,c='black')
plt.plot(x_coord, y_coord, label="Крицкий-Менкель", c='red', linewidth=0.8)

plt.xlabel("Обеспеченность, Р%")
plt.ylabel("Расход воды, м^3/с")
plt.title("Кривая обеспеченностей")

plt.xticks(x_coord, xticks_combined, rotation=90)

y_tick_interval = 1  # Установить нужный интервал !!!
min_value_y = 0
max_value_y = max(y_coord)
ytick_positions = list(range(int(min_value_y), int(max_value_y) + 2, y_tick_interval))
#plt.yticks(ytick_positions)

plt.legend()
plt.grid()
plt.show()