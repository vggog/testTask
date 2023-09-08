from vkbottle.bot import Message

from src.bot import bot
from src.states import StartState, TodayTomorrowState
from src.keyboards import get_menu_button, get_two_buttons_inline_keyboard
from src.repository import Repo


@bot.on.private_message(text="Начать")
async def start(message: Message):
    repo = Repo()
    if repo.get_user(message.from_id):
        await message.answer(
            "Приветствую))",
            keyboard=get_menu_button(),
        )
        return

    await message.answer("Введите ваш город:")
    await bot.state_dispenser.set(message.peer_id, StartState.SITY)


@bot.on.private_message(state=StartState.SITY)
async def upload_sity(message: Message):
    repo = Repo()

    repo.add_user(
        message.from_id,
        message.text
    )

    await message.answer(
        "Ваш город сохранён.",
        keyboard=get_menu_button(),
    )


@bot.on.private_message(text="Погода")
async def weather_first_step(message: Message):
    await message.answer(
        "На какой день вам нужен прогноз погоды?",
        keyboard=get_two_buttons_inline_keyboard(
            "Сегодня",
            "Завтра",
        )
    )

    await bot.state_dispenser.set(message.peer_id, TodayTomorrowState.WHEN)


@bot.on.private_message(state=TodayTomorrowState.WHEN)
async def get_weather(message: Message):
    print("Залез")
    repo = Repo()

    user_info = repo.get_user(user_id=message.from_id)
    if not user_info:
        await message.answer("Вы не зарегистрированы.")
        await message.answer('Напишите "Начать"')
        return

    weather_when = message.text
    sity = user_info[1]

    if weather_when == "Сегодня":
        await message.answer(f"Погода в {sity} сегодня.")
    elif weather_when == "Завтра":
        await message.answer(f"Погода в {sity} завтра.")
    else:
        await message.answer("Неверный ввод.")
