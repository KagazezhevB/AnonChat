import telebot
from constants import TOKEN, SEARCH_COMPANION, STOP_SEARCH
from database import Database
from keyboards import search_companion_markup, stop_search_markup


db = Database("database/db.db")
bot = telebot.TeleBot(token=TOKEN)


@bot.message_handler(commands=["start"])
def start_message(message):
    bot.send_message(message.chat.id, f"Привет {message.from_user.first_name} {message.from_user.last_name}",
                     reply_markup=search_companion_markup)


@bot.message_handler(commands=["menu"])
def menu(message):
    bot.send_message(message.chat.id, "", reply_markup=search_companion_markup)


@bot.message_handler(content_types=["text"])
def bot_message(message):
    if message.text == SEARCH_COMPANION:
        db.add_queue(message.chat.id)
        bot.send_message(message.chat.id, "", reply_markup=stop_search_markup)

    elif message.text == STOP_SEARCH:
        db.delete_queue(message.chat.id)
        bot.send_message(message.chat.id, "", reply_markup=search_companion_markup)


bot.polling()
