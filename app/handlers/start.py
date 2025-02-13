from aiogram import Router, types
from aiogram.filters import Command

router = Router(name="start")

@router.message(Command(commands=["start"]))
async def start_command(message: types.Message):
    """
    Handles the /start command.

    :param message: Message object containing the /start command.
    :type message: types.Message
    """

    user_name = message.from_user.full_name
    await message.answer(f"Hello, {user_name}🖐️\n"
                         f"\nI can save photos📷 to Yandex Disk.\n"
                         f"\nSend me photos📷 that need to be saved or forward them to the chat.")
