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


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет, я бот, который ведет статистику\n'
                                      'выпадения чисел в рулетке. Я показываю, какие числа\n'
                                      'и с какой вероятностью выпадают после введенного вами числа.\n\n'
                                      'Как это работает: вы вводите в текст сообщения <u>число</u>,\n'
                                      'далее выводится список и вероятность выпадения\n'
                                      'чисел, которые уже выпадали после заданного значения.\n\n'
                                      'Я поддерживаю следующие команды:\n'
                                      '/go - перезапуск бота\n'
    # '/help - помощь\n'
    # '/list - напечатать текущий список чисел, по которым ведется статистика\n'
    # '/length - длина списка.\n\n'
                                      'Чтобы начать - жми комманду /go\n'
                                      'Если бот в процессе работы зависнет, можно ввести эту же команду.')


@bot.message_handler(commands=['go'])
def go(message):
    bot.send_message(message.chat.id, 'Я готов к работе. Введите число:')
    bot.register_next_step_handler(message, main)


# markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
# hidden_markup = types.ReplyKeyboardRemove()
# item_list = types.KeyboardButton('Список чисел')
# item_length = types.KeyboardButton('Длина списка')
# markup.add(item_list, item_length)

# @bot.message_handler(func=lambda m: True)
#     def next_step(message):
#         if message.text == 'Список чисел':
#             bot.send_message(message.chat.id, f'Список: {list_number}')
#             bot.send_message(message.chat.id, 'Введите следующее число:') #reply_markup=hidden_markup
#             bot.register_next_step_handler(message, main)
#
#     elif message.text == 'Длина списка':
#     bot.send_message(message.chat.id, f'Длина списка: {len(list_number)}')
#     bot.send_message(message.chat.id, 'Введите следующее число:') #reply_markup=hidden_markup
#     bot.register_next_step_handler(message, main)


def main(message):
    global number
    number = int(message.text)
    global list_number
    answer_text = 'После введеного числа выпадали:\n'
    list_number.append(number)
    next_numbers = next_number_list(number, list_number)
    duplicate_list = delete_duplicate_number(next_numbers)
    if next_numbers == []:
        keyboard = types.InlineKeyboardMarkup()
        next_num = types.InlineKeyboardButton(text='Следующее число', callback_data='next')
        print_list = types.InlineKeyboardButton(text='Список чисел', callback_data='list')
        length_list = types.InlineKeyboardButton(text='Длина списка', callback_data='length')
        keyboard.add(next_num, print_list, length_list)
        bot.send_message(message.chat.id, 'Этого числа еще нет в статистике', reply_markup=keyboard)
    else:
        for i in range(len(duplicate_list)):
            count_num = next_numbers.count(duplicate_list[i])
            percent = (count_num / len(next_numbers)) * 100
            percent = round(percent, 2)
            answer_text += 'Число ' + str(duplicate_list[i]) + ' ' + '(' + str(count_num) + 'раз) - ' + str(
                percent) + '%\n'
            if i == len(duplicate_list) - 1:
                keyboard = types.InlineKeyboardMarkup()
                next_num = types.InlineKeyboardButton(text='Следующее число', callback_data='next')
                print_list = types.InlineKeyboardButton(text='Список чисел', callback_data='list')
                length_list = types.InlineKeyboardButton(text='Длина списка', callback_data='length')
                keyboard.add(next_num, print_list, length_list)
                bot.send_message(message.chat.id, answer_text, reply_markup=keyboard)  # reply_markup=markup
            else:
                continue
    # bot.register_next_step_handler(message, main)


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == 'next':
        bot.send_message(call.message.chat.id, 'Введите следующее число:')
        bot.register_next_step_handler(call.message, main)
    elif call.data == 'list':
        bot.send_message(call.message.chat.id, f'Список: {list_number}')
        bot.send_message(call.message.chat.id, 'Введите следующее число:')
        bot.register_next_step_handler(call.message, main)
    elif call.data == 'length':
        bot.send_message(call.message.chat.id, f'Длина списка: {len(list_number)}')
        bot.send_message(call.message.chat.id, 'Введите следующее число:')
        bot.register_next_step_handler(call.message, main)


bot.infinity_polling()
