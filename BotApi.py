"""
Пока можем реальзовывать в произвольном стиле.
Думаю начать надо с инициальзации бота.
Прописать /start
Потом организовать прослушку сообщений боту
Следующий шаг обработка сообщений
"""


import logging
from aiogram import Bot, Dispatcher, executor, types  # pip install aiogram
from aiogram.dispatcher.filters import Text

# Объект бота
bot = Bot(token="5070557333:AAE095ix1EIyFPJcX4k0u3IyOfNNZOD3hoQ")
# Диспетчер для бота
dp = Dispatcher(bot)
# Включаем логирование, я пока не очень разобрался чё как оно работает
logging.basicConfig(level=logging.INFO)


# Хэндлер на команду /start
@dp.message_handler(commands="start")
async def cmd_start(message: types.Message):
    await message.answer("👨🏻‍💻Привет!\n\nСюда можно прислать любую новость:  текст, фото, видео и аудио.\n\n"
                         "💁 Вызвать такси или 🍕 Заказать еду")
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["📣 Предложить новость", "🚕 Вызвать такси", "🍕 Заказать еду"]
    keyboard.add(*buttons[0:2])
    keyboard.add(buttons[2])
    await message.answer("⌨️ Выбери что хотите сделать:", reply_markup=keyboard)


# Хэндлер на команду /type
@dp.message_handler(commands="type")
async def cmd_type(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["📣 Предложить новость", "🚕 Вызвать такси", "🍕 Заказать еду"]
    keyboard.add(*buttons[0:2])
    keyboard.add(buttons[2])
    await message.answer("⌨️ Выбери что хотите сделать:", reply_markup=keyboard)


# Хэндлер на команду Вызвать такси
@dp.message_handler(Text(equals="🚕 Вызвать такси"))
async def cmd_news(message: types.Message):
    await message.answer(
        "🚕 Такси Молния: +79542281337\nОт 100 рублей", reply_markup=types.ReplyKeyboardRemove())

# Хэндлер на команду Предложить новость
@dp.message_handler(Text(equals="📣 Предложить новость"))
async def cmd_news(message: types.Message):
    await message.answer(
        "📣 Предложить новость. Всегда можно изменить свой выбор "
        "по команде /type, или просто перезапустив бота - команда /start.\n\n "
        "Расскажи, что произошло?", reply_markup=types.ReplyKeyboardRemove())

# Хэндлер на команду Заказать еду..
@dp.message_handler(Text(equals="🍕 Заказать еду"))
async def cmd_news(message: types.Message):
    await message.answer(
        "🍕 Сити пицца: +79542281337\nОт 54 рублей", reply_markup=types.ReplyKeyboardRemove())

if __name__ == "__main__":
    # Запуск бота..
    executor.start_polling(dp, skip_updates=True)