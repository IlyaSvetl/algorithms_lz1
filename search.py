import random  as rm           #импортируем

start_list = []                #создадим рандомный список
while len(start_list) < 100:
    n = rm.randint(0, 1_000_000) 
    if n not in start_list:        #смотрим чтобы не было дубликатов
        start_list.append(n)       #если такого же элемента нет в списке добавляем его если такого эл. нет в списке то мы добовляем его туда

print(f'Список (начальный) {start_list}')        # Изначальный список 
start_list.sort()                                #сортируем список
print(f' Список(отсортированный) {start_list}')  # Отсортированный список

comparison_l = 0                                     # поиск (линейный)
y = int(input('Введите число которое хотите найти: '))
if y in start_list:                                  #делаем проверку на искомый элемент в списке
    for i in range(0,len(start_list)):               # проходим по всем эл. списка и сравниваем, не является ли этот элемент списка искомым 
        comparison_l += 1
        if y == start_list[i]:
            index_l = i
            break
    print(f'По линейному поиску \n Индекс вашего числа в списке {index_l}, ваше число {index_l+1} по счёту \n Количество сравнений {comparison_l}')
else:
    print('Вашего числа нет')

print('='*150)

comparison_b = 0                                     #бинарный поиск
first = 0
last = len(start_list)-1
index_b = -1

if y in start_list:                                  #делаем проверку есть ли этот(искомый) элемент в списке
    while (first <= last) and (index_b == -1):       #ищем по поиску(бинарному)
        mid = (first+last)//2
        if start_list[mid] == y:
            index_b = mid
        else:
            if y<start_list[mid]:         
                last = mid -1
            else:
                first = mid +1
            comparison_b += 1
        comparison_b += 1 
    print(f'По бинарному поиску \n Индекс вашего числа в списке {index_b}, ваше число {index_b+1} по счёту \n Количество сравнений {comparison_b}')
else:
    print('Вашего числа нету в списке')