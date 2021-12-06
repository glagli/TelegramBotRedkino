from aiogram import types


# Хэндлер на команду /start
def start (dp, keyboard):
    @dp.message_handler(commands="start")
    async def cmd_start (message: types.Message):
        await message.answer("👨🏻‍💻Привет!\n\nСюда можно прислать любую новость:  текст, фото, видео и аудио.\n\n"
                             "💁 Вызвать такси или 🍕 Заказать еду")
        await message.answer("⌨️ Выбери что хотите сделать:", reply_markup=keyboard)
