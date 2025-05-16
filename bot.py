from aiogram import Bot, Dispatcher, types
import asyncio

API_TOKEN = "7549706885:AAGRJuC317xNQHuV3A_s_i5ohruXVtNMOS0"

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

@dp.message()
async def respond_roll(message: types.Message):
    if message.text and message.text.lower() == "obervorlaring":
        await message.answer("🧻")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
