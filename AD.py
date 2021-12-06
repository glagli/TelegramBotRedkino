from aiogram import types
from aiogram.dispatcher.filters import Text


# Хэндлер на команду Заказать еду..
def ad (dp, keyboard):
    @dp.message_handler(Text(equals="Реклама"))
    async def cmd_ad (message: types.Message):
        await message.answer(
            "По поводу рекламы - @RedkinoAD", reply_markup=types.ReplyKeyboardRemove())
        await message.answer("⌨️ Выбери что хотите сделать:", reply_markup=keyboard)
