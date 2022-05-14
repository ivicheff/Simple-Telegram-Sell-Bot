from aiogram import types, Dispatcher
from create_bot import dp, bot
from keyboards import kb_client
from aiogram.types import ReplyKeyboardRemove
from database import sqlite_db


async def command_start(message : types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Bon appetit', reply_markup=kb_client)
        await message.delete()
    except:
        await message.reply('Talk to bot, write him:\nhttps://t.me/PizzaBot')

async def pizza_open_command(message : types.Message):
    await bot.send_message(message.from_user.id, 'Вс-Чт с 9:00 до 20:00')

async def pizza_place_command(message : types.Message):
    await bot.send_message(message.from_user.id, 'Backer str, 15')

@dp.message_handler(commands=['Menu'])
async def pizza_menu_command(message : types.Message):
   await sqlite_db.sql_read(message)

def register_handlers_client(dp:Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'help'])
    dp.register_message_handler(pizza_open_command, commands=['open'])
    dp.register_message_handler(pizza_place_command, commands=['place'])
    dp.register_message_handler(pizza_menu_command, commands=['menu'])