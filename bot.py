from aiogram import Bot, Dispatcher, types
from aiogram.filters import Text
from aiogram.types import Message
import asyncio

API_TOKEN = "7549706885:AAGRJuC317xNQHuV3A_s_i5ohruXVtNMOS0"

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

@dp.message(Text(equals="obervorlaring", ignore_case=True))
async def respond_roll(message: Message):
    await message.answer("🧻")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
