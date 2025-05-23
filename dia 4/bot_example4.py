import json
import os
from datetime import datetime

from bot import bot

users = {
    123456: {
        "first_name": "Juan",
        "last_name": "Pérez",
        "username": "juanito",
        "language": "es",
        "registration_date": "2023-10-30 14:00:00",
        "is_bot": False,
        "warnings": 0,
    }
}
ADMINS = [123456, 789012]


def save_users():
    with open("users.json", "w", encoding="utf-8") as f:
        json.dump(users, f, ensure_ascii=False, indent=4)


if os.path.exists("users.json"):
    with open("users.json", "r", encoding="utf-8") as f:
        users = json.load(f)


@bot.message_handler(commands=["register"])
def register_user(message):
    user_id = message.from_user.id
    users[user_id] = {
        "first_name": message.from_user.first_name,
        "last_name": message.from_user.last_name,
        "username": message.from_user.username,
        "language_code": message.from_user.language_code,
        "is_bot": message.from_user.is_bot,
        "registration_date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "warnings": 0,
        "chat_id": message.chat.id,
        "chat_type": message.chat.type,
    }
    save_users()

    bot.reply_to(
        message,
        f"✅ *Registro exitoso*:\n"
        f"- Nombre: `{message.from_user.first_name}`\n"
        f"- Usuario: @{message.from_user.username}\n"
        f"- ID: `{user_id}`\n"
        f"- Fecha: `{users[user_id]['registration_date']}`",
        parse_mode="Markdown",
    )


@bot.message_handler(commands=["myinfo"])
def show_user_info(message):
    user_id = message.from_user.id
    if user_id in users:
        user_data = users[user_id]
        response = (
            "📋 *Tu información*:\n"
            f"- Nombre: `{user_data['first_name']} {user_data.get('last_name', '')}`\n"
            f"- Usuario: @{user_data['username']}\n"
            f"- ID: `{user_id}`\n"
            f"- Registrado el: `{user_data['registration_date']}`\n"
            f"- Advertencias: `{user_data['warnings']}`"
        )
    else:
        response = "❌ No estás registrado. Usa /register."

    bot.reply_to(message, response, parse_mode="Markdown")


@bot.message_handler(commands=["buscar"])
def search_user(message):
    if len(message.text.split()) > 1:
        search_term = message.text.split()[1].lower()
        results = [
            f"👤 {data['first_name']} (@{data['username']}) - ID: `{uid}`"
            for uid, data in users.items()
            if (
                search_term in data["first_name"].lower()
                or (data["username"] and search_term in data["username"].lower())
            )
        ]
        bot.reply_to(
            message,
            f"🔍 *Resultados para '{search_term}'*:\n" + "\n".join(results)
            if results
            else "No se encontraron coincidencias.",
            parse_mode="Markdown",
        )
    else:
        bot.reply_to(message, "⚠️ Usa: /buscar [nombre o usuario]")


# Comando para admins: listar todos los usuarios
@bot.message_handler(commands=["listar_usuarios"])
def list_users(message):
    if message.from_user.id not in ADMINS:
        return

    users_list = [
        f"{i + 1}. {data['first_name']} (@{data['username']}) - ID: `{uid}`"
        for i, (uid, data) in enumerate(users.items())
    ]
    bot.send_message(
        message.chat.id,
        f"👥 *Usuarios registrados ({len(users)})*:\n" + "\n".join(users_list),
        parse_mode="Markdown",
    )


if __name__ == "__main__":
    bot.polling()
