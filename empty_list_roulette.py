list_number = [1, 2, 3]
while True:
    print()
    number = int(input('Введите число: '))
    next_number_list = []

    for i in range(len(list_number)):
        if i == len(list_number) - 1:
            continue
        elif list_number[i] == number:
            next_number_list.append(list_number[i + 1])
    list_number.append(number)
    duplicate = set(next_number_list)
    duplicate_list = []

    for i in duplicate:
        duplicate_list.append(i)
    print('После числа', number, 'выпадали:')
    for num in range(len(duplicate_list)):
        count_num = next_number_list.count(duplicate_list[num])
        percent = (count_num / len(next_number_list)) * 100
        print('Число -', duplicate_list[num], '(' + str(count_num), 'раз) -', round(percent, 2), '%')
