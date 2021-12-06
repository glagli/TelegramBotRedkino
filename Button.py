from aiogram import types


def buttonFunctions ():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["📣 Предложить новость", "🚕 Вызвать такси", "🍕 Заказать еду", "Реклама"]
    keyboard.add(*buttons[0:3])
    keyboard.add(buttons[3])
    return keyboard
