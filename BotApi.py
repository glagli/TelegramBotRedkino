from aiogram import executor  # pip install aiogram
from Init import init
from Button import buttonFunctions
from Start import start
from Taxi import taxi
from Food import food
from AD import ad
from News import news

tokenVladG = "5089204526:AAHl0aN_0BqvVo_0yf8F6ys5_zGhSycT4ww"  # тестовый бот ВладГ
tokenProd = "5070557333:AAE095ix1EIyFPJcX4k0u3IyOfNNZOD3hoQ"  # тестовый бот Основа


bot, dp = init(tokenVladG)
keyboard = buttonFunctions()


# start
start(dp, keyboard)

# Предложить новость
news(dp, keyboard, bot)

# Вызвать такси
taxi(dp, keyboard)

# Реклама
ad(dp, keyboard)

# Заказать еду..
food(dp, keyboard, bot)


if __name__ == "__main__":
    # Запуск бота.
    executor.start_polling(dp, skip_updates=True)
