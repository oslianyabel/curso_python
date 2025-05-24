from bot import bot
from utils import load_file

"""
Recuerden los mensajes del usuario son procesados solo por la primera funcion de arriba hacia abajo que cumpla con el decorador
Errores comunes:
- usen este decorador solo para la ultima función: @bot.message_handler(func=lambda message: True) De lo contrario nunca se procesarán funciones definidas debajo de esta
- No pueden definir 2 funciones con el mismo nombre
- Comprueben que se esté cargando el token correctamente
- Los comandos no pueden contener espacios
"""


@bot.message_handler(content_types=["document", "photo", "audio", "video", "voice"])
def handle_files(message):
    if message.document:  # Documentos (PDF, ZIP, etc.)
        file_id = message.document.file_id
        file_info = bot.get_file(file_id)
        downloaded_file = bot.download_file(file_info.file_path)
        load_file(downloaded_file, "archivo.pdf")

        bot.reply_to(message, "📄 Documento descargado!")

    elif message.photo:  # Fotos (JPEG, PNG)
        file_id = message.photo[-1].file_id  # La última es la de mayor calidad
        file_info = bot.get_file(file_id)
        downloaded_file = bot.download_file(file_info.file_path)
        load_file(downloaded_file, "foto.jpg")

        bot.reply_to(message, "📸 Foto descargada!")

    elif message.audio:  # Audio (MP3)
        file_id = message.audio.file_id
        file_info = bot.get_file(file_id)
        downloaded_file = bot.download_file(file_info.file_path)
        load_file(downloaded_file, "audio.mp3")

        bot.reply_to(message, "🎵 Audio descargado!")

    elif message.video:  # Video (MP4)
        file_id = message.video.file_id
        file_info = bot.get_file(file_id)
        downloaded_file = bot.download_file(file_info.file_path)
        load_file(downloaded_file, "video.mp4")

        bot.reply_to(message, "🎥 Video descargado!")

    elif message.voice:  # Nota de voz (OGG)
        file_id = message.voice.file_id
        file_info = bot.get_file(file_id)
        downloaded_file = bot.download_file(file_info.file_path)
        load_file(downloaded_file, "nota_de_voz.ogg")

        bot.reply_to(message, "🎤 Nota de voz descargada!")


@bot.message_handler(commands=["reenviar"])
def reenviar_archivo(message):
    chat_id = message.chat.id
    file_id = "FILE_ID_DEL_ARCHIVO"  # Supongamos que ya tenemos un file_id (obtenido previamente)

    bot.send_document(chat_id, file_id)
    bot.send_photo(chat_id, file_id)
    bot.send_audio(chat_id, file_id)
    bot.send_video(chat_id, file_id)


if __name__ == "__main__":
    bot.delete_webhook()
    print("Bot Ready!")
    bot.polling()
    print("Bot Stopped!")
