from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.dispatcher.filters import Text
import os


storage=MemoryStorage()

bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher(bot, storage=storage)

# answ = dict()
#
# urlkb = InlineKeyboardMarkup(row_width=2)
# urlButton = InlineKeyboardButton(text='Link', url='https://youtube.com')
# urlButton2 = InlineKeyboardButton(text='Link2', url='https://google.com')
# x = [InlineKeyboardButton(text='Link3', url='https://google.com'), InlineKeyboardButton(text='Link4', url='https://google.com'),\
#      InlineKeyboardButton(text='Link5', url='https://google.com')]
# urlkb.add(urlButton, urlButton2).row(*x).insert(InlineKeyboardButton(text='Link6', url='https://google.com'))
#
# @dp.message_handler(commands='links')
# async def url_command(message : types.Message):
#     await message.answer('Links: ', reply_markup=urlkb)
#
#
# inkb = InlineKeyboardMarkup(row_width=1).add(InlineKeyboardButton(text='Like', callback_data='like_1'),\
#                                     InlineKeyboardButton(text='he like', callback_data='like_-1'))
#
# @dp.message_handler(commands='test')
# async def test_commands(message : types.Message):
#     await message.answer('Inline button', reply_markup=inkb)
#
# @dp.callback_query_handlers(Text(startswith='like_'))
# async def www_call(callback : types.CallbackQuery):
#     res = int(callback.text.split('_')[1])
#     if callback.from_user.id not in answ:
#         answ[f'{callback.from_user.id}'] = res
#         await callback.answer('You are voted')
#     else:
#         await callback.answer('You are alredy voted', show_alert=True)