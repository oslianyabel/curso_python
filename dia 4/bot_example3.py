from bot import bot
from utils import ban_words

"""
Para que un bot pueda eliminar mensajes o banear usuarios de un grupo debe ser nombrado administrador. Aplica también para canales
Recuerden los mensajes del usuario son procesados solo por la primera funcion de arriba hacia abajo que cumpla con el decorador
Errores comunes:
- usen este decorador solo para la ultima función: @bot.message_handler(func=lambda message: True) De lo contrario nunca se procesarán funciones definidas debajo de esta
- No pueden definir 2 funciones con el mismo nombre
- Comprueben que se esté cargando el token correctamente
- Los comandos no pueden contener espacios
"""


def ban_user_decision(message):
    text = message.text.lower() if message.text else ""
    for word in ban_words:
        if word in text:
            return True

    return False


@bot.message_handler(func=ban_user_decision)
def ban_user(message):
    chat_id = message.chat.id
    user_id = message.reply_to_message.from_user.id

    if message.chat.type in ["group", "supergroup"]:
        try:
            bot.delete_message(
                chat_id, message.reply_to_message.message_id
            )  # se elimina el mensaje
            bot.ban_chat_member(chat_id, user_id)
            bot.send_message(chat_id, "⛔ Usuario baneado")
        except Exception as e:
            bot.send_message(chat_id, f"Error: {e}")
    else:
        bot.send_message(chat_id, "Si estuvieras en mi grupo te botara")


@bot.message_handler(commands=["enviar_canal"])
def send_to_channel(message):
    CHANNEL_ID = "@nombre_de_tu_canal"
    bot.send_message(CHANNEL_ID, "Hello World")


@bot.message_handler(func=lambda message: True)  # Captura todos los mensajes
def handle_group_messages(message):
    chat_type = message.chat.type
    chat_id = message.chat.id

    if chat_type in ["group", "supergroup"]:
        group_name = message.chat.title
        members_count = bot.get_chat_members_count(chat_id)
        bot.send_message(
            chat_id, f"🔍 Grupo: {group_name}\n👥 Miembros: {members_count}"
        )
    elif chat_type == "channel":
        bot.reply_to(message, "¡Mensaje recibido en un canal!")
    else:
        bot.reply_to(message, "¡Mensaje en chat privado!")
