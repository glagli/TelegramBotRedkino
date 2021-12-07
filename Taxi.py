from aiogram import types
from aiogram.dispatcher.filters import Text


# Хэндлер на команду Вызвать такси
def taxi(dp, keyboard):
    @dp.message_handler(Text(equals="🚕 Вызвать такси"))
    async def cmd_taxi(message: types.Message):
        await message.answer(
            "🚕 Такси Молния: +79112223334\nДля размещения рекламы такси писать сюда -> @RedkinoAD",
            reply_markup=types.ReplyKeyboardRemove())
        await message.answer("⌨️ Выбери что хотите сделать:", reply_markup=keyboard)
