from aiogram import Router, types

router = Router(name="other")

@router.message()
async def handle_other_messages(message: types.Message):
    user_name = message.from_user.full_name
    await message.answer(f"{user_name}❗\n"
                         f"\nЯ умею сохранять фото и видео📷.\n"
                         f"\nПрикрепи в чат ❗фото/видео/документ❗ или перешли их мне.")
