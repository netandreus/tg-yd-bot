from PIL import Image
from io import BytesIO

from aiogram import Router, F, Bot
from aiogram.types import ContentType, Message

from app.services.yandex_disk import upload


router = Router(name="photo")

@router.message(F.content_type == ContentType.PHOTO)
async def handle_photo(message: Message, bot: Bot):
    """
    Handles photo messages, uploads them to Yandex Disk.

    :param message: Message object containing the photo.
    :type message: Message
    :param bot: Bot object for interacting with Telegram API.
    :type bot: Bot
    """

    photo = message.photo[-1]
    file_info = await bot.get_file(photo.file_id)

    with BytesIO() as byte_stream:
        await bot.download_file(file_info.file_path, destination=byte_stream)
        byte_stream.seek(0)
        extension = get_file_extension(byte_stream)
        if extension:
            filename = photo.file_id + extension
        else:
            filename = photo.file_id

        byte_stream.seek(0)
        result = upload(byte_stream, filename)

        if result:
            await message.answer("Photo " + filename + " uploaded successfully 🙌")
        else:
            await message.answer("Error when uploading")


def get_file_extension(byte_stream):
    """
    Returns the file extension (including the dot) for an image given as a byte stream.

    Parameters:
        byte_stream: A bytes-like object or a file-like stream containing image data.

    Returns:
        A string with the file extension (e.g., '.jpg', '.png') or None if detection fails.
    """
    # If byte_stream is not already a stream, wrap it with BytesIO.
    if not hasattr(byte_stream, 'read'):
        byte_stream = BytesIO(byte_stream)

    try:
        with Image.open(byte_stream) as img:
            # Get the image format (e.g., 'JPEG', 'PNG', etc.)
            img_format = img.format
    except Exception as e:
        print("Error detecting image format:", e)
        return None

    if not img_format:
        return None

    # Standardize the extension for JPEG images.
    if img_format.upper() == 'JPEG':
        return '.jpg'

    # For other formats, return the lowercase format as extension.
    return '.' + img_format.lower()
