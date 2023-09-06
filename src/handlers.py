from vkbottle.bot import Message

from src.bot import bot


@bot.on.message(text="Начать")
async def start(message: Message):
    print("good!")
