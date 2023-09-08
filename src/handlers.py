from vkbottle.bot import Message

from src.bot import bot
from src.states import StartState
from src.keyboards import get_menu_button
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

