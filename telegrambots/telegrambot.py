#importing main aiogram biblioteq
from aiogram import Dispatcher, Bot, types, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
#importing functions, path from task2 file
from aiogram.utils.keyboard import InlineKeyboardBuilder
from task2 import get_photo_urls
from task2 import files_func
from task2 import folder_path
#importing os for work with operation system, and creat a directory with photo
import os
#...
import asyncio
#importing random for set a random name for photo files
import random



from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, KeyboardButtonRequestUser
photo_for_now = 0
photo_rating = {}
rating_photo = 0
def keyboard():
    button = ReplyKeyboardMarkup(keyboard=[
        [
        
        KeyboardButton(text = 'help'),
        KeyboardButton(text = 'random_photo'),
        KeyboardButton(text='vip'),
        KeyboardButton(text='all count of message')
        ]
        ]
    )
    return button

def rating_key():
    but = ReplyKeyboardMarkup(keyboard=[
[
        KeyboardButton(text="1"),
        KeyboardButton(text="2"),
        KeyboardButton(text="3"),
        KeyboardButton(text="4"),
        KeyboardButton(text="5"),
]]
    )
    return but

def test_button():
    builder = InlineKeyboardBuilder()
    for i in range(1, 6):
        builder.button(text=f"{i}", callback_data=f'{i}')
        
        builder.adjust(1, 2)
    return builder

from messages import MESSAGES
#initialising bot and set token for Bot
bot = Bot(token=MESSAGES.get('TOKEN', "token is not found"))
dp = Dispatcher()
#initialising function get_photo_urls
photo_urls = get_photo_urls()

random_photo_url = random.choice(photo_urls)
rate_dict = {}

async def init_photo_for_now():
    global photo_for_now
    photo_for_now = await dp.storage.get_data(key=0) or 0

# Функция для обновления значения переменной photo_for_now и сохранения его в хранилище
async def update_photo_for_now():
    global photo_for_now
    await dp.storage.set_data(key=0, data=photo_for_now)
    
#write a logic for command /start
@dp.message(CommandStart())
async def start_command(message:Message):
    await bot.send_video(chat_id=message.from_user.id, video=MESSAGES.get("url_2", 'url_2 is not found'))
    await message.answer(MESSAGES.get("start", "Command 'start' not found in messages file"), reply_markup=keyboard())


@dp.message(F.text == 'vip')
async def vip_message(message: Message):
    await message.answer("Hello it's a premium message for you")

#here we set random photo
last_sent_message = None
async def send_random_photo(message:Message):
    global last_sent_message
    last_sent_message = message 
    print("Inside send_random_photo")
    global photo_for_now
    count_ph = message.text.split()
    count_photo = 1
    if len(count_ph) > 1:
        try:
            count_photo = int(count_ph[1])
            if count_photo < 1:
                await message.answer("*please provide a valid count of photo*", parse_mode="Markdown")
                return
        except ValueError:
            await message.answer("please provide a valid count of photo", parse_mode="Markdown")
            return

    if len(photo_urls) > 0:
        for _ in range(int(count_photo)):
            random_photo_url = random.choice(photo_urls)  
            
            
            files_func(random_photo_url)
            await bot.send_photo(message.chat.id, photo=random_photo_url)
            photo_for_now += 1
            photo_urls.remove(random_photo_url)  
            rate_dict[random_photo_url] = [] 
    else:
        # Если список фотографий исчерпан, выбираем новую случайную фотографию из всех доступных
        random_photo_url = random.choice(get_photo_urls())
        files_func(random_photo_url)
        await bot.send_photo(message.chat.id, photo=random_photo_url)
        photo_for_now += 1

        rate_dict[random_photo_url] = []
    return random_photo_url
async def send():
    global last_sent_message, random_photo_url
    if last_sent_message:
        await send_random_photo(last_sent_message)
        await last_sent_message.answer("rate photo", reply_markup=test_button().as_markup())
        

# async def rating(message:Message):
#     global random_photo_url
#     await message.answer(rand_photo)

@dp.callback_query(lambda callback_query: callback_query.data in ['1', '2', '3', '4', '5'])
async def callback_handler(callback_query: types.CallbackQuery):
    data = callback_query.data
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, text=data)
    await send()
    global random_photo_url
    # phot_url = callback_query.message.photo[-1].file_id
    # print(phot_url)
    await bot.send_message(chat_id=callback_query.from_user.id, text="Ваш ответ", reply_to_message_id=callback_query.message.message_id-1)
    
    #if phot_url in rate_dict:
        #rate_dict[phot_url].append(data)
    
    # rate_dict[phot_url] = data
    # await bot.send_photo(callback_query.from_user.id, photo=phot_url)
    
    print(rate_dict)
    

#here we use command random_photo for sending it for user
@dp.message(Command('random_photos'))
async def handle_photo(message: Message):
    if not os.path.exists(folder_path):
        files_func(random_photo_url)
    else:
        print(f"Папка 'downfile' вже існує.")
    await message.answer("your photo")
    await send_random_photo(message)
    

@dp.message(F.text == 'random_photo')
async def rand_photo(message: Message):
    # global photo_for_now
    await send_random_photo(message)
    await message.answer("rate this photo", reply_markup=test_button().as_markup())
    # photo_for_now += 1
#here is a command help that have all information about bot and commands that it have
@dp.message(F.text == 'help')
async def help_command(message:Message):
    await bot.send_video(chat_id=message.from_user.id, video=MESSAGES.get("url_1", "url_1 is not found"), caption=MESSAGES.get("help", "Command 'help' not found"))
    await message.answer("*hello i'ts  a help command for you*", parse_mode='Markdown')

    # await message.answer(MESSAGES.get("help", "Command 'help' not found"))



@dp.message(F.text == "all count of message")
async def count_of_photo(message: Message):
    await message.answer(f'photo that we have in database{len(photo_urls)}')
    await message.answer(f"*for now bot send {photo_for_now}*", parse_mode='Markdown')


#running bot
async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)
    await init_photo_for_now()

if __name__ == '__main__':
    asyncio.run(main())
    
print(rate_dict)
