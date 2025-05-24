from bot import bot
from telebot import types

"""
Recuerden los mensajes del usuario son procesados solo por la primera funcion de arriba hacia abajo que cumpla con el decorador
Errores comunes:
- usen este decorador solo para la ultima función: @bot.message_handler(func=lambda message: True) De lo contrario nunca se procesarán funciones definidas debajo de esta
- No pueden definir 2 funciones con el mismo nombre
- Comprueben que se esté cargando el token correctamente
- Los comandos no pueden contener espacios
"""


# vias para enviar un msg
@bot.message_handler(commands=["HelloWorld"])
def send_welcome(message):
    bot.send_chat_action(message.chat_id, "typing")

    # 2 formas de enviar un msg
    bot.reply_to(message, "Hello World")
    bot.send_message(message.chat_id, "Hello World")

    # envio de msgs con formatos especiales
    """
    *Negrita*
    _Cursiva_
    `Código`
    [Enlace](https://google.com)
    """
    bot.send_message(message.chat_id, "*Hello World*", parse_mode="MarkdownV2")

    """
    <b>Negrita</b>
    <i>Cursiva</i>
    <code>Código</code>
    <a href="https://google.com">Enlace</a>
    """
    bot.send_message(message.chat_id, "<b>Hello World</b>", parse_mode="HTML")

    # envio de teclado
    markup = types.ReplyKeyboardMarkup(row_width=3)
    btn1 = types.KeyboardButton("Option1")
    btn2 = types.KeyboardButton("Option2")
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, "Elige una opción:", reply_markup=markup)

    # envio de botonera
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton("Google", url="https://google.com")
    btn2 = types.InlineKeyboardButton("Presióname", callback_data="btn_pressed")
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, "Botones inline:", reply_markup=markup)


# Manejar eventos de botones inline:
@bot.callback_query_handler(func=lambda call: True)
def handle_callback(call):
    if call.data == "btn_pressed":
        bot.answer_callback_query(call.id, "¡Botón presionado!")


@bot.edited_message_handler(func=lambda message: True)
def handle_edited_messages(message):
    bot.reply_to(message, "Editaste el mensaje")
