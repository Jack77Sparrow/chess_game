import aiogram
from aiogram import types, Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
import asyncio
bot = Bot(token="6319103400:AAEuv0bl6KFALVpDngLFT2wHcOxq5mVSRto")
dp = Dispatcher()


admin = [1813205201]
@dp.message(CommandStart())
async def start(message: Message):
    if message.from_user.id in admin:
        await bot.send_message()
    await bot.send_message(message.from_user.id, "hello world")
    await bot.send_message(message.from_user.id, f'{message.from_user.id}')

# @dp.message(Command("admin"))
# async def admin(message:Message):
    
    
#running bot
async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)
    

if __name__ == '__main__':
    asyncio.run(main())
    
