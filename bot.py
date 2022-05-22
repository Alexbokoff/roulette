import telebot
from telebot import types
from config import TOKEN
from list import list_number

bot = telebot.TeleBot(TOKEN, parse_mode='html')
list_number = list_number
number = 0


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


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == 'list':
        keyboard = types.InlineKeyboardMarkup()
        btn_go = types.InlineKeyboardButton(text='Продолжить работу', callback_data='go')
        length_list = types.InlineKeyboardButton(text='Длина списка', callback_data='length')
        keyboard.add(btn_go, length_list)
        bot.send_message(call.message.chat.id, f'Список: {list_number} \n\n'
                                               f'Работа приостановлена, для продолжения нажмите необходимую кнопку ниже:',
                         reply_markup=keyboard)
    elif call.data == 'length':
        keyboard = types.InlineKeyboardMarkup()
        btn_go = types.InlineKeyboardButton(text='Продолжить работу', callback_data='go')
        print_list = types.InlineKeyboardButton(text='Список чисел', callback_data='list')
        keyboard.add(btn_go, print_list)
        bot.send_message(call.message.chat.id, f'Длина списка: {len(list_number)}\n\n'
                                               f'Работа приостановлена, для продолжения нажмите необходимую кнопку ниже:',
                         reply_markup=keyboard)
    elif call.data == 'go':
        bot.send_message(call.message.chat.id, 'Я готов к работе. Введите число:')
        bot.register_next_step_handler(call.message, main)


@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.InlineKeyboardMarkup()
    btn_go = types.InlineKeyboardButton(text='Начать работу', callback_data='go')
    print_list = types.InlineKeyboardButton(text='Список чисел', callback_data='list')
    length_list = types.InlineKeyboardButton(text='Длина списка', callback_data='length')
    keyboard.add(btn_go, print_list, length_list)
    bot.send_message(message.chat.id, 'Привет, я бот, который ведет статистику\n'
                                      'выпадения чисел в рулетке.\n'
                                      'Вы находитесь в главном меню.\n'
                                      'Тут можно посмотреть список чисел, а также длинну списка\n\n'
                                      'Для начала работы, нажми необходимую кнопку ниже:\n', reply_markup=keyboard)


def main(message):
    text = message.text.lower()
    if text == 'главное меню':
        start(message)
    elif text == 'start':
        start(message)
    elif text == 'go':
        start(message)
    elif not text.isdigit():
        bot.send_message(message.chat.id, 'Данные должны быть числом, повторите ввод')
        bot.register_next_step_handler(message, main)
    elif int(message.text) < 37 and int(message.text) >= 0:
        global number
        number = int(message.text)
        global list_number
        answer_text = 'После введеного числа выпадали:\n'
        list_number.append(number)

        add_number_to_list = str(list_number)
        file = open('list_number.txt', 'w')
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
            for i in range(len(duplicate_list)):
                count_num = next_numbers.count(duplicate_list[i])
                percent = (count_num / len(next_numbers)) * 100
                percent = round(percent, 2)
                answer_text += 'Число ' + str(duplicate_list[i]) + ' ' + '(' + str(count_num) + 'раз) - ' + str(
                    percent) + '%\n'
                if i == len(duplicate_list) - 1:
                    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
                    menu_btn = types.KeyboardButton('Главное меню')
                    keyboard.add(menu_btn)
                    bot.send_message(message.chat.id, answer_text, reply_markup=keyboard)
                    bot.register_next_step_handler(message, main)
                else:
                    continue
    elif int(message.text) > 36 or int(message.text) < 0:
        bot.send_message(message.chat.id, 'Неверное числовое значение, повторите ввод')
        bot.register_next_step_handler(message, main)


bot.infinity_polling()
