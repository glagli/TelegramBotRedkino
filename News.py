from aiogram import types
from aiogram.dispatcher.filters import Text


# Хэндлер на команду Предложить новость
def news(dp, keyboard, bot):
    @dp.message_handler(Text(equals="📣 Предложить новость"))
    async def cmd_news(message: types.Message):
        await message.answer(
            "📣 Предложить новость\nВсегда можно изменить свой выбор "
            "перезапустив бота - команда /start.\n\n "
            "Расскажи, что произошло?", reply_markup=types.ReplyKeyboardRemove())

        @dp.message_handler(content_types=["photo"])
        async def send_photo(message: types.Message):
            photo_id = message.photo[-1].file_id
            message.from_user.id = -1001674751308
            await bot.send_photo(message.from_user.id, photo_id, caption=message.caption)
            await message.answer("👀 Ваш пост успешно принят\n"
                                 "Хотите что-то ещё рассказать?")
            await message.answer("⌨️ Выбери что хотите сделать:", reply_markup=keyboard)

        @dp.message_handler(content_types=["document"])
        async def send_file(message: types.Message):
            file_id = message.document.file_id
            message.from_user.id = -1001674751308
            await bot.send_document(message.from_user.id, file_id, caption=message.caption)
            await message.answer("👀 Ваш пост успешно принят\n"
                                 "Хотите что-то ещё рассказать?")
            await message.answer("⌨️ Выбери что хотите сделать:", reply_markup=keyboard)

        @dp.message_handler()
        async def any_text_message2(message: types.Message):
            print(message)
            message.text = f"Публикация от пользователя @{message.from_user.username} \n\n{message.text}"
            message.from_user.id = -1001674751308
            await bot.send_message(message.from_user.id, message.text)
            await message.answer("👀 Ваш пост успешно принят\n"
                                 "Хотите что-то ещё рассказать?")
            await message.answer("⌨️ Выбери что хотите сделать:", reply_markup=keyboard)
