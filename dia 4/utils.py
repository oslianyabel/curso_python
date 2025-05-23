from telebot import types

from bot import bot

ban_words = ["futbol", "pelota", "basket", "baloncesto", "tenis", "boxeo"]


def send_keyboard(message, options: list, row_width=3):
    markup = types.ReplyKeyboardMarkup(row_width=row_width)
    for o in options:
        btn = types.KeyboardButton(o)
        markup.add(btn)

    bot.send_message(message.chat.id, "Elige una opción:", reply_markup=markup)


def load_file(downloaded_file, name):
    with open(name, "wb") as new_file:
        new_file.write(downloaded_file)
