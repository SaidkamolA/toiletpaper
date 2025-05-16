import logging
from aiogram import Bot, Dispatcher, types
import asyncio

API_TOKEN = "7549706885:AAGRJuC317xNQHuV3A_s_i5ohruXVtNMOS0"

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

@dp.message()
async def respond_roll(message: types.Message):
    logging.info(f"Получено сообщение: {message.text}")
    if message.text and message.text.lower() == "obervorlaring":
        await message.answer("🧻")
        logging.info("Ответил эмодзи 🧻")

async def main():
    logging.info("Запуск бота...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
