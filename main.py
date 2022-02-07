import telebot
from telebot import types
from config import TOKEN

SEARCH_COMPANION = "Поиск собеседника"
STOP_SEARCH = "Остановить поиск"

bot = telebot.TeleBot(token=TOKEN)


@bot.message_handler(commands=["start"])
def start_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    search_button = types.KeyboardButton(SEARCH_COMPANION)
    markup.add(search_button)
    bot.send_message(message.chat.id, f"Привет {message.from_user.first_name} {message.from_user.last_name}",
                     reply_markup=markup)


@bot.message_handler(commands=["menu"])
def menu(message):
    if message.text == SEARCH_COMPANION:
        markup1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        stop_search_button = types.KeyboardButton(STOP_SEARCH)
        markup1.add(stop_search_button)
        bot.send_message(message.chat.id, "Поиск собеседника", reply_markup=markup1)


bot.polling()
