import telebot
from telebot import types
from operator import itemgetter
from config import TOKEN_test
from list_test_bot import list_number

bot = telebot.TeleBot(TOKEN_test, parse_mode='html')
list_number = list_number


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
    if len(duplicate_list) == 0:
        percent_even = 0
        percent_odd = 0
        return percent_even, percent_odd
    elif odd_number != 0 and even_number != 0:
        percent_odd = (odd_number / len(duplicate_list)) * 100
        percent_even = (even_number / len(duplicate_list)) * 100
        return percent_even, percent_odd
    elif odd_number == 0:
        percent_odd = 0
        percent_even = (even_number / len(duplicate_list)) * 100
        return percent_even, percent_odd
    else:
        percent_even = 0
        percent_odd = (odd_number / len(duplicate_list)) * 100
        return percent_even, percent_odd


def sector_number(duplicate_list, summ_list):
    jeu_0 = [12, 35, 3, 26, 0, 32, 15]
    voisins = [22, 18, 29, 7, 28, 19, 4, 21, 2, 25]
    orphelins = [1, 20, 14, 31, 9, 17, 34, 6]
    tiers = [27, 13, 36, 11, 30, 8, 23, 10, 5, 24, 16, 33]

    list_jeu_0 = [0, 0]
    list_voisins = [0, 0]
    list_orphelins = [0, 0]
    list_tiers = [0, 0]

    for i_number in duplicate_list:
        for index1 in jeu_0:
            if index1 == i_number:
                list_jeu_0[0] += 1
                for index in range(len(summ_list)):
                    if index1 == summ_list[index][0]:
                        list_jeu_0[1] += summ_list[index][1]
                        break

        for index2 in voisins:
            if index2 == i_number:
                list_voisins[0] += 1
                for index in range(len(summ_list)):
                    if index2 == summ_list[index][0]:
                        list_voisins[1] += summ_list[index][1]
                        break

        for index3 in orphelins:
            if index3 == i_number:
                list_orphelins[0] += 1
                for index in range(len(summ_list)):
                    if index3 == summ_list[index][0]:
                        list_orphelins[1] += summ_list[index][1]
                        break

        for index4 in tiers:
            if index4 == i_number:
                list_tiers[0] += 1
                for index in range(len(summ_list)):
                    if index4 == summ_list[index][0]:
                        list_tiers[1] += summ_list[index][1]
                        break

    return list_jeu_0, list_voisins, list_orphelins, list_tiers


def sorted_result(duplicate_list, next_numbers, percent_even, percent_odd, answer_text):
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
        answer_text += str(summ_list[i_num][0]) + ' - ' + '( ' + str(
            summ_list[i_num][1]) + ' раз )__ ' + str(summ_list[i_num][2]) + '%\n'
    answer_text += 'Четное: ' + str(round(percent_even, 2)) + '%, Нечетное: ' + str(round(percent_odd, 2)) + '%\n\n'
    return answer_text, summ_list


def output_result(answer_text, list_jeu_0, list_voisins, list_orphelins, list_tiers, list_first_12,
                  list_second_12, list_third_12):
    answer_text += 'Сектора:\n'
    answer_text += 'Zero (' + str(list_jeu_0[0]) + ' чисел) - ' + str(list_jeu_0[1]) + 'раз\n' \
                    'Voisins (' + str(list_voisins[0]) + ' чисел) - ' + str(list_voisins[1]) + 'раз\n' \
                    'Orphelins (' + str(list_orphelins[0]) + 'чисел) - ' + str(list_orphelins[1]) + 'раз\n' \
                     'Tiers (' + str(list_tiers[0]) + ' чисел) - ' + str(list_tiers[1]) + 'раз\n\n'
    answer_text += 'Дюжины:\n'
    answer_text += '1 st 12 (' + str(list_first_12[0]) + ' чисел) - ' + str(list_first_12[1]) + ' раз\n'
    answer_text += '2 st 12 (' + str(list_second_12[0]) + ' чисел) - ' + str(list_second_12[1]) + ' раз\n'
    answer_text += '3 st 12 (' + str(list_third_12[0]) + ' чисел) - ' + str(list_third_12[1]) + ' раз\n\n'

    return answer_text


def delete_last_number(message):
    list_number.pop(-1)
    bot.send_message(message.chat.id, 'Последнее число списка удалено.\n'
                                      'Введите следующее число')
    bot.register_next_step_handler(message, main)


def last_100_numbers(list_number):
    last_list = []
    last_range = len(list_number) - (len(list_number) - 100)
    for index in range(last_range, 0, -1):
        last_list.append(list_number[-index])
    return last_list


def dozen(summ_list):
    first_12 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    second_12 = [13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]
    third_12 = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36]

    list_first_12 = [0, 0]
    list_second_12 = [0, 0]
    list_third_12 = [0, 0]

    for i_number in range(len(summ_list)):
        for index1 in first_12:
            if index1 == summ_list[i_number][0]:
                list_first_12[0] += 1
                list_first_12[1] += summ_list[i_number][1]
                break
        for index2 in second_12:
            if index2 == summ_list[i_number][0]:
                list_second_12[0] += 1
                list_second_12[1] += summ_list[i_number][1]
                break
        for index3 in third_12:
            if index3 == summ_list[i_number][0]:
                list_third_12[0] += 1
                list_third_12[1] += summ_list[i_number][1]
                break
    return list_first_12, list_second_12, list_third_12


def next_five_numbers(number, list_number, answer_text):
    next_five_numbers = []  # [2, 3, 2, 4, 5, 7, 7, 8, 3, 3, 16, 18, 18, 21]
    count_number = list_number.count(number)
    answer_text += '5 Следующих чисел:\n'
    for i in range(len(list_number)):
        if i == len(list_number) - 1:
            continue
        elif list_number[i] == number:
            for next in range(1, 6):
                if i + next > len(list_number) - 1:
                    break
                else:
                    next_five_numbers.append(list_number[i + next])

    delete_duplicate_list = list(set(next_five_numbers))  # [2, 3, 4, 5, 7, 8, 16, 18, 21]
    summ_list = []
    temp_list = []
    for i in delete_duplicate_list:
        temp_list.append(i)
        temp_list.append(next_five_numbers.count(i))
        summ_list.append(temp_list)  # [[2, 2], [3, 3], [4, 1], [5, 1], [7, 2], [8, 1], [16, 1], [18, 2], [21, 1]]
        temp_list = []

    summ_list = sorted(summ_list, key=itemgetter(1), reverse=True)
    for i in summ_list:
        if i[1] / count_number > 0.22 and i[1] > 1:
            answer_text += str(i[0]) + ' - ' + str(i[1]) + ' раз\n'
        else:
            continue
    answer_text += '\n'

    return answer_text


def add_keyboard():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    menu_btn = types.KeyboardButton('Главное меню')
    keyboard.add(menu_btn)
    return keyboard


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == 'length':
        keyboard = types.InlineKeyboardMarkup()
        btn_go = types.InlineKeyboardButton(text='Продолжить работу', callback_data='go')
        keyboard.add(btn_go)
        bot.send_message(call.message.chat.id, f'Длина списка: {len(list_number)}\n\n'
                                               f'Работа приостановлена, для продолжения нажмите кнопку «Продолжить работу»',
                         reply_markup=keyboard)
        bot.answer_callback_query(call.id, "Length list print")
    elif call.data == 'go':
        bot.send_message(call.message.chat.id, 'Я готов к работе. Введите число:')
        bot.answer_callback_query(call.id, "Ready to go")
        bot.register_next_step_handler(call.message, main)


@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.InlineKeyboardMarkup()
    btn_go = types.InlineKeyboardButton(text='Начать работу', callback_data='go')
    length_list = types.InlineKeyboardButton(text='Длина списка', callback_data='length')
    keyboard.add(btn_go, length_list)
    bot.send_message(message.chat.id, 'Вы находитесь в главном меню.\n\n'
                                      'Поддерживаемые команды:\n'
                                      '<b>start</b> - выход в главное меню\n'
                                      '<b>del</b> - удаление последнего числа в списке. '
                                      'Для этого нужно отправить боту сообщение с текстом «del»\n\n'
                                      'Для начала работы, нажми необходимую кнопку ниже:\n', reply_markup=keyboard)


def main(message):
    text = message.text.lower()
    if text == 'del':
        delete_last_number(message)
    elif text == 'главное меню':
        start(message)
    elif text == 'start':
        start(message)
    elif not text.isdigit():
        bot.send_message(message.chat.id, 'Данные должны быть числом, повторите ввод')
        bot.register_next_step_handler(message, main)
    elif int(message.text) < 37 and int(message.text) >= 0:
        global number
        number = int(message.text)
        global list_number
        list_number.append(number)

        add_number_to_list = str(list_number)
        file = open('list_test_bot.txt', 'w')
        file.write(add_number_to_list)
        file.close()

        next_numbers = next_number_list(number, list_number)
        duplicate_list = delete_duplicate_number(next_numbers)
        if next_numbers == []:
            keyboard = add_keyboard()
            bot.send_message(message.chat.id, 'Статистики нет', reply_markup=keyboard)
            bot.register_next_step_handler(message, main)
        else:
            answer_text = 'Число ' + str(number) + ' выпадало: ' + str(list_number.count(number)) + ' раз\n'
            answer_text += 'После него выпадало: ' + str(len(duplicate_list)) + ' чисел\n'
            percent_even, percent_odd = what_is_number(duplicate_list)
            answer_text, summ_list = sorted_result(duplicate_list, next_numbers, percent_even, percent_odd, answer_text)
            list_jeu_0, list_voisins, list_orphelins, list_tiers = sector_number(duplicate_list, summ_list)
            list_first_12, list_second_12, list_third_12 = dozen(summ_list)
            answer_text = output_result(answer_text, list_jeu_0, list_voisins, list_orphelins, list_tiers,
                                        list_first_12,
                                        list_second_12, list_third_12)
            answer_text = next_five_numbers(number, list_number, answer_text)
            # Последние 100 чисел
            if len(list_number) > 100:
                last_list = last_100_numbers(list_number)
                next_numbers = next_number_list(number, last_list)
                if next_numbers == []:
                    keyboard = add_keyboard()
                    answer_text += 'За последние 100 ходов статистики нет\n'
                    bot.send_message(message.chat.id, answer_text, reply_markup=keyboard)
                    bot.register_next_step_handler(message, main)
                else:
                    duplicate_list = delete_duplicate_number(next_numbers)
                    answer_text += 'За последние 100 ходов число ' + str(number) + ' выпадало: ' + \
                                   str(last_list.count(number)) + ' раз\n'
                    answer_text += 'После него выпадало: ' + str(len(duplicate_list)) + ' чисел\n'
                    percent_even, percent_odd = what_is_number(duplicate_list)
                    answer_text, summ_list = sorted_result(duplicate_list, next_numbers, percent_even, percent_odd,
                                                           answer_text)
                    list_jeu_0, list_voisins, list_orphelins, list_tiers = sector_number(duplicate_list, summ_list)
                    list_first_12, list_second_12, list_third_12 = dozen(summ_list)
                    answer_text = output_result(answer_text, list_jeu_0, list_voisins, list_orphelins, list_tiers,
                                                list_first_12, list_second_12, list_third_12)
                    answer_text = next_five_numbers(number, last_list, answer_text)
                    keyboard = add_keyboard()
                    bot.send_message(message.chat.id, answer_text, reply_markup=keyboard)
                    bot.register_next_step_handler(message, main)
            else:
                keyboard = add_keyboard()
                bot.send_message(message.chat.id, answer_text, reply_markup=keyboard)
                bot.register_next_step_handler(message, main)

    elif int(message.text) > 36 or int(message.text) < 0:
        bot.send_message(message.chat.id, 'Неверное числовое значение, повторите ввод')
        bot.register_next_step_handler(message, main)


bot.infinity_polling()
