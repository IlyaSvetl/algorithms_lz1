import random as rm

start_list = []        #создаём рандомный список
for i in range(0,100):
    start_list.append(rm.randint(0, 1_000_000))
print(f'Начальный список {start_list}')
comparison_p = 0

#сортируем список пузырьковым методом
sorted_list_p = start_list.copy()
stop_flag = True
while stop_flag is True:
    stop_flag = False
    for i in range(0, len(sorted_list_p) - 1):
        if sorted_list_p[i] < sorted_list_p[i + 1]:
            swap = sorted_list_p[i]
            sorted_list_p[i] = sorted_list_p[i + 1]
            sorted_list_p[i + 1] = swap
            print(f'Промежуточный список {sorted_list_p}')    #промежуточный вывод
            stop_flag = True
        comparison_p += 1                                      #кол-во сравнений

print('='*150)

comparison_v = 0
unsorted_list = start_list
sorted_list_v = []


while len(unsorted_list) > 0:    #сортируем список методом выборки
    max = unsorted_list[0]
    for i in range(0, len(unsorted_list)):
        if unsorted_list[i] > max:
            max = unsorted_list[i]
        comparison_v += 1      #кол-во сравнений
    sorted_list_v.append(max)
    unsorted_list.remove(max)
    print(f'Промежуточный начальный список {unsorted_list} \n Промежуточный отсортированный список {sorted_list_v}')   #промежуточный вывод

#Выводим значения
print('='*150)
print(f'Отсортированный список по убыванию пузырьковым методом {sorted_list_p}\n Число сравнений {comparison_p}')

print('='*150)
print(f'Отсортированный список по убыванию методом выборки {sorted_list_v}\n Число сравнений {comparison_v}')


