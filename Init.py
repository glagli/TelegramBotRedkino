import logging
from aiogram import Bot, Dispatcher


def init(token):
    bot = Bot(token=token)  # тестовый бот Основа
    # Диспетчер для бота
    dp = Dispatcher(bot)
    # Включаем логирование, я пока не очень разобрался чё как оно работает
    logging.basicConfig(level=logging.INFO)
    return bot, dp
