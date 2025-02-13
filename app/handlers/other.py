from aiogram import Router, types

router = Router(name="other")

@router.message()
async def handle_other_messages(message: types.Message):
    user_name = message.from_user.full_name
    await message.answer(f"{user_name}❗\n"
                         f"\nI can save photos and videos📷.\n"
                         f"\nAttach ❗photo/video/document❗ to the chat or forward them to me.")
