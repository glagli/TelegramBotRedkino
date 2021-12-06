from aiogram import types
from aiogram.dispatcher.filters import Text


# Хэндлер на команду Заказать еду..
def food (dp, keyboard, bot):
    @dp.message_handler(Text(equals="🍕 Заказать еду"))
    async def cmd_food (message: types.Message):
        p = open("test.jpg", "rb")
        await bot.send_photo(message.chat.id, p,
                             "🍕 Сити пицца: +79112223344\nДля размещения рекламы кафе писать сюда -> @RedkinoAD")
        await message.answer("⌨️ Выбери что хотите сделать:", reply_markup=keyboard)
