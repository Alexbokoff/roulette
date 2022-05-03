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
    bot.send_message(message.chat.id, 'Я готов к работе. Введите число')
    bot.register_next_step_handler(message, main)


markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
hidden_markup = types.ReplyKeyboardRemove()
item_list = types.KeyboardButton('Список чисел')
item_length = types.KeyboardButton('Длина списка')
markup.add(item_list, item_length)


def main(message):
    global number
    number = int(message.text)
    global list_number
    answer_text = ''
    list_number.append(number)
    next_numbers = next_number_list(number, list_number)
    duplicate_list = delete_duplicate_number(next_numbers)

    bot.send_message(message.chat.id, 'После введеного числа выпадали:')
    for i in range(len(duplicate_list)):
        count_num = next_numbers.count(duplicate_list[i])
        percent = (count_num / len(next_numbers)) * 100
        percent = round(percent, 2)
        answer_text += 'Число ' + str(duplicate_list[i]) + ' ' + '(' + str(count_num) + 'раз) - ' + str(percent) + '%\n'
        if i != len(duplicate_list) - 1:
            continue
        else:
            bot.send_message(message.chat.id, answer_text, reply_markup=markup)

    @bot.message_handler(content_types=['text'])
    def next_step(message):
        if message.text == 'Список чисел':
            bot.send_message(message.chat.id, f'Список: {list_number}')
            bot.send_message(message.chat.id, 'Введите следующее число', reply_markup=hidden_markup)
            bot.register_next_step_handler(message, main)
        elif message.text == 'Длина списка':
            bot.send_message(message.chat.id, f'Длина списка: {len(list_number)}')
            bot.send_message(message.chat.id, 'Введите следующее число', reply_markup=hidden_markup)
            bot.register_next_step_handler(message, main)

    bot.send_message(message.chat.id, 'Введите следующее число')
    bot.register_next_step_handler(message, main)


bot.infinity_polling()
