from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

b1 = KeyboardButton('/open')
b2 = KeyboardButton('/place')
b3 = KeyboardButton('/menu')
# b4 = KeyboardButton('Share number', request_contact=True)
# b5 = KeyboardButton('Where am I?', request_location=True)

kb_client = ReplyKeyboardMarkup(resize_keyboard=True)

kb_client.add(b1).add(b2).add(b3)#.row(b4, b5)