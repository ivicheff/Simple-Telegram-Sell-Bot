﻿# simple_telegram_bot

create start_bot.bat file above project with the following code:

@echo off

call %~dp0PizzaSheffBot\venv\Scripts\activate

cd %~dp0PizzaSheffBot

set TOKEN=

python bot_telegram.py

pause

create folder "images" with pictures you want to show to the client
