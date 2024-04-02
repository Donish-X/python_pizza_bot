from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
import asyncio

bot = Bot(token='6633343715:AAFRj6zIRzQKq8v7ozf91qLQbHWdB4ZthvA')
dp = Dispatcher()

@dp.message(CommandStart())
async def start_cmd(message: types.Message):
    await message.answer("Это была команда старт")
    

@dp.message()
async def echo(message: types.Message):
    await message.answer(message.text)
    
    

async def main() -> None:
    await bot.delete_webhook()
    await dp.start_polling(bot)
    

asyncio.run(main())