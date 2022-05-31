from list_roulette import list_number
from operator import itemgetter


def next_number_list(number, list_number):
    next_numbers = []
    for i in range(len(list_number)):
        if i == len(list_number) - 1:
            continue
        elif list_number[i] == number:
            next_numbers.append(list_number[i + 1])
    return next_numbers


def delete_duplicate_number(next_numbers):
    duplicate_list = list(set(next_numbers))
    return duplicate_list


def what_is_number(duplicate_list):
    odd_number = 0
    even_number = 0
    for number in duplicate_list:
        if number % 2 == 1:
            odd_number += 1
        else:
            even_number += 1
    percent_odd = (odd_number / len(duplicate_list)) * 100
    percent_even = (even_number / len(duplicate_list)) * 100
    return percent_even, percent_odd


def sorted_result(duplicate_list, next_numbers, percent_even, percent_odd):
    answer_text = ''
    summ_list = []
    for i in range(len(duplicate_list)):
        num_list = []
        count_num = next_numbers.count(duplicate_list[i])
        percent = (count_num / len(next_numbers)) * 100
        percent = round(percent, 2)
        num_list.append(duplicate_list[i])
        num_list.append(count_num)
        num_list.append(percent)
        summ_list.append(num_list)

    summ_list = sorted(summ_list, key=itemgetter(2), reverse=True)

    for i_num in range(len(summ_list)):
        answer_text += str(summ_list[i_num][0]) + ' - ' + str(
            summ_list[i_num][1]) + ' раз: ' + str(summ_list[i_num][2]) + '%\n'
    answer_text += 'Четное: ' + str(round(percent_even, 2)) + '%, Нечетное: ' + str(round(percent_odd, 2)) + '%\n'
    return answer_text


def output_result(answer_text):
    print('После введеного числа выпадали:', end='\n')
    print(answer_text)


def delete_number():
    list_number.pop(-1)
    print('Последнее число списка удалено')


def main(number):
    list_number.append(number)
    add_number = str(list_number)
    file = open('list_roulette.txt', 'w')
    file.write(add_number)
    file.close()

    next_numbers = next_number_list(number, list_number)
    duplicate_list = delete_duplicate_number(next_numbers)
    percent_even, percent_odd = what_is_number(duplicate_list)
    answer_text = sorted_result(duplicate_list, next_numbers, percent_even, percent_odd)
    output_result(answer_text)
    print()


while True:
    number = input('Введите число: ')
    if number.lower() == 'del':
        delete_number()
    elif int(number) >= 0 and int(number) <= 36:
        main(int(number))
    elif int(number) < 0 or int(number) > 36:
        print('Неверное значение')
