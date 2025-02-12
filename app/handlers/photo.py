from io import BytesIO

from aiogram import Router, F, Bot
from aiogram.types import ContentType, Message

from app.services.yandex_disk import upload


router = Router(name="photo")

@router.message(F.content_type == ContentType.PHOTO)
async def handle_photo(message: Message, bot: Bot):
    """
    Обрабатывает сообщения с фотографиями, загружает их на Яндекс Диск.

    :param message: Объект сообщения, содержащий фотографию.
    :type message: Message
    :param bot: Объект бота для взаимодействия с Telegram API.
    :type bot: Bot
    """

    photo = message.photo[-1]
    file_info = await bot.get_file(photo.file_id)

    with BytesIO() as byte_stream:
        await bot.download_file(file_info.file_path, destination=byte_stream)
        byte_stream.seek(0)
        result = upload(byte_stream, photo.file_id)

        if result:
            await message.answer("Photo uploaded successfully 🙌")
        else:
            await message.answer("Error when uploading")
