def next_number_list(number, list_number):
    next_numbers = []
    for i in range(len(list_number)):
        if i == len(list_number) - 1:
            continue
        elif list_number[i] == number:
            next_numbers.append(list_number[i + 1])
    return next_numbers


def delete_duplicate_number(next_numbers):
    duplicate_delele = set(next_numbers)
    duplicate_list = []
    for i in duplicate_delele:
        duplicate_list.append(i)
    return duplicate_list


def output_result(number, duplicate_list, next_numbers):
    print('После числа', number, 'выпадали:')
    for i in range(len(duplicate_list)):
        count_num = next_numbers.count(duplicate_list[i])
        percent = (count_num / len(next_numbers)) * 100
        print('Число -', duplicate_list[i], '(' + str(count_num), 'раз) -', round(percent, 2), '%')


list_number = []
while True:
    number = int(input('Введите число: '))
    next_numbers = next_number_list(number, list_number)
    list_number.append(number)
    duplicate_list = delete_duplicate_number(next_numbers)
    output_result(number, duplicate_list, next_numbers)
    print()
