from aiogram import types
from aiogram.dispatcher.filters import Text


# Хэндлер на команду Предложить новость
def news (dp, keyboard, bot):
    @dp.message_handler(Text(equals="📣 Предложить новость"))
    async def cmd_news(message: types.Message):
        await message.answer(
            "📣 Предложить новость\nВсегда можно изменить свой выбор "
            "перезапустив бота - команда /start.\n\n "
            "Расскажи, что произошло?", reply_markup=types.ReplyKeyboardRemove())

        # for number in range(1):
        @dp.message_handler()  # Вложенность позволила включить прослушивание только когда выбранно Предложить новость. Пока не могу сообразить как ограничить кол-во сообщений
        async def any_text_message2(message: types.Message):
            message.text = f"Публикация от пользователя @{message.from_user.username} \n\n{message.text}"
            message.from_user.id = -1001674751308
            await bot.send_message(message.from_user.id, message.text)
            #await message.answer("Информация отправляется, ожидайте...")
            #time.sleep(5) можно задержку так сделать, но не спасёт если чел все равно будет писать много
            # print(message.text)
            # await message.answer("fmt.quote_html(message.text)</b>", parse_mode=types.ParseMode.HTML)
            await message.answer("👀 Ваш пост успешно принят\n"
                                 "Хотите что-то ещё рассказать?")
            await message.answer("⌨️ Выбери что хотите сделать:", reply_markup=keyboard)
