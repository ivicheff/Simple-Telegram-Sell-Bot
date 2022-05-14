from aiogram.utils import executor
from create_bot import dp
from database import sqlite_db

async def on_startup(_):
    print('Bot is online')
    sqlite_db.sql_start()

from handlers import client, admin, other

client.register_handlers_client(dp)
admin.register_handlers_admin(dp)
other.register_handlers_other(dp)

executor.start_polling(dp, skip_updates=True, on_startup=on_startup)


# from aiogram import Bot, types
# from aiogram.dispatcher import Dispatcher
# from aiogram.utils import executor
#
# import os
#
# bot = Bot(token=os.getenv('TOKEN'))
# dp = Dispatcher(bot)
#
# async def on_startup(_):
#     print('Bot is online')
#
#
# @dp.message_handler(commands=['start', 'help'])
# async def command_start(message : types.Message):
#     try:
#         await bot.send_message(message.from_user.id, 'Bon appetit')
#         await message.delete()
#     except:
#         await message.reply('Talk to bot, write him:\nhttps://t.me/PizzaBot')
#
# @dp.message_handler(commands=['Open_hours'])
# async def pizza_open_command(message : types.Message):
#     await bot.send_message(message.from_user.id, 'Вс-ЧТ с 9:00 до 20:00')
#
# @dp.message_handler(commands=['Place'])
# async def pizza_place_command(message : types.Message):
#     await bot.send_message(message.from_user.id, 'Backer str, 15')
#
#
# @dp.message_handler()
# async def echo_send(message : types.Message):
#     if message.text == 'Hello':
#         await message.answer('Hello to you!')
#
# executor.start_polling(dp, skip_updates=True, on_startup=on_startup)