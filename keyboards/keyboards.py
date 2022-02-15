from telebot import types
from constants import SEARCH_COMPANION, STOP_SEARCH


def create_search_companion_markup():
    markup1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    search_button = types.KeyboardButton(SEARCH_COMPANION)
    return markup1.add(search_button)


def create_stop_search_markup():
    markup1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    stop_search_button = types.KeyboardButton(STOP_SEARCH)
    return markup1.add(stop_search_button)


search_companion_markup = create_search_companion_markup()
stop_search_markup = create_stop_search_markup()

