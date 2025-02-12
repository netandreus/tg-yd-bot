from aiogram import BaseMiddleware

from app.config import ALLOWED_USERS


class AccessMiddleware(BaseMiddleware):
    """
    Проверяет, есть ли у пользователя доступ к функционалу бота.
    Если пользователь не в списке разрешенных, отправляет сообщение об отсутствии доступа.
    """

    async def __call__(self, handler, event, data):
        """
        Вызывается для каждого события, проверяет доступ пользователя.
        """

        user_id = event.from_user.id
        if user_id not in ALLOWED_USERS:
            await event.answer("😔 У Вас нет доступа.")
            return
        return await handler(event, data)
