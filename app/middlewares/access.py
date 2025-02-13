from aiogram import BaseMiddleware

from app.config import ALLOWED_USERS


class AccessMiddleware(BaseMiddleware):
    """
    Checks if the user has access to the bot's functionality.
    If the user is not in the allowed users list, sends an access denied message.
    """

    async def __call__(self, handler, event, data):
        """
        Called for each event, checks user access.
        """

        user_id = event.from_user.id
        if user_id not in ALLOWED_USERS:
            await event.answer("😔 У Вас нет доступа.")
            return
        return await handler(event, data)
