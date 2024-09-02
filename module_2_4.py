'''
Дегтярев Виталий (группа 22/08)
Домашнее задание №2.04
Домашняя работа по уроку "Цикл for. Элементы списка. Полезные функции в цикле"
'''
# Задание списка чисел
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
# Задание пустых списков
primes, no_primes = [], []

# Блок логики
for number in numbers: # Перебираем элементы исходного списка
    if number == 1:
        continue  # С 1-цей не работаем - пропускаем
    is_prime = True # Задание флага обнаружения простого числа
    for i in range(2, number): # Перебираем делители текущего числа из исходного списка
        if number % i == 0:
            is_prime = False # 'Устанавливем флаг - что число не простое'
            no_primes.append(number) # Пополняем список не простых чисел
            break # Дальнейший поиск можно прервать, т.к. делитель найден
    if is_prime == True: # Если флаг остался не изменен - значит текущее число оказалось простым
        primes.append(number)  # Пополняем тогда список простых чисел

# Вывод результатов в консоль
print(f'Был задан следующий исходный список чисел: {numbers} - из них:\nПростые числа: {primes}\nНепростые числа: {no_primes}')
            
            