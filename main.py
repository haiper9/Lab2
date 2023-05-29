import asyncio
import logging

from aiogram import Bot, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.dispatcher import Dispatcher
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.webhook import SendMessage
from aiogram.types import User, InputFile, Message, message, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils import executor
import parser

API_TOKEN = ''
logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
numImageMotivation = 2


@dp.message_handler(commands="start")
async def start_bot(message: types.Message, keyboard: object = None):
    await message.answer(f"Привет, {message.from_user.full_name}", reply_markup=keyboard)
    kb = [
        [
            types.KeyboardButton(text="Мотивируй!")
        ],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder=""
    )
    await message.answer("Я могу мотивировать тебя для увеличения уверености в своих силах!", reply_markup=keyboard)


@dp.message_handler(Text(equals="Мотивируй!"))
async def motivation(message: types.Message):
    global numImageMotivation
    url = parser.listImagesUrl.get(numImageMotivation)
    print(url)
    await bot.send_photo(message.chat.id, photo=url)
    numImageMotivation += 1



if __name__ == '__main__':
    parser.parse()
    executor.start_polling(dp, skip_updates=True)