from aiogram import types, Dispatcher
from create_bot import dp

async def echo_send(message : types.Message):
    async def echo_send(message: types.Message):
        if message.text == 'Hello':
            await message.answer('Hello to you!')
            await message.delete()

def register_handlers_other(dp : Dispatcher):
    dp.register_message_handler(echo_send)