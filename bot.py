import telebot
from telebot import types
from operator import itemgetter
from config import TOKEN
from list_bot import list_number

bot = telebot.TeleBot(TOKEN, parse_mode='html')
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
    percent_odd = (odd_number / len(duplicate_list)) * 100
    percent_even = (even_number / len(duplicate_list)) * 100
    return percent_even, percent_odd


def sorted_result(duplicate_list, next_numbers, percent_even, percent_odd):
    answer_text = 'После введеного числа выпадали:\n'
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
    answer_text += 'Четное: ' + str(round(percent_even, 2)) + '%, Нечетное: ' + str(round(percent_odd, 2)) + '%\n'
    return answer_text


def delete_last_number(message):
    list_number.pop(-1)
    bot.send_message(message.chat.id, 'Последнее число списка удалено.\n'
                                      'Введите следующее число')
    bot.register_next_step_handler(message, main)


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == 'length':
        keyboard = types.InlineKeyboardMarkup()
        btn_go = types.InlineKeyboardButton(text='Продолжить работу', callback_data='go')
        keyboard.add(btn_go)
        bot.send_message(call.message.chat.id, f'Длина списка: {len(list_number)}\n\n'
                                               f'Работа приостановлена, для продолжения нажмите кнопку «Продолжить работу»',
                         reply_markup=keyboard)
    elif call.data == 'go':
        bot.send_message(call.message.chat.id, 'Я готов к работе. Введите число:')
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
        file = open('list_bot.txt', 'w')
        file.write(add_number_to_list)
        file.close()

        next_numbers = next_number_list(number, list_number)
        duplicate_list = delete_duplicate_number(next_numbers)
        if next_numbers == []:
            keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
            menu_btn = types.KeyboardButton('Главное меню')
            keyboard.add(menu_btn)
            bot.send_message(message.chat.id, 'Этого числа еще нет в статистике', reply_markup=keyboard)
            bot.register_next_step_handler(message, main)
        else:
            percent_even, percent_odd = what_is_number(duplicate_list)
            answer_text = sorted_result(duplicate_list, next_numbers, percent_even, percent_odd)

            keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
            menu_btn = types.KeyboardButton('Главное меню')
            keyboard.add(menu_btn)

            bot.send_message(message.chat.id, answer_text, reply_markup=keyboard)
            bot.register_next_step_handler(message, main)

    elif int(message.text) > 36 or int(message.text) < 0:
        bot.send_message(message.chat.id, 'Неверное числовое значение, повторите ввод')
        bot.register_next_step_handler(message, main)


bot.infinity_polling()
