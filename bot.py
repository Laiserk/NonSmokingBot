import time

from typing import List

from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

TOKEN = "Token"

bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot)

button_yes = InlineKeyboardButton(text="Да", callback_data="yes")
button_no = InlineKeyboardButton(text="Нет", callback_data="no")

keyboard_inline = InlineKeyboardMarkup().add(button_yes, button_no)


async def ask(message):
    await message.reply("Ты курил сегодня?", reply_markup=keyboard_inline)


@dp.message_handler(commands=["start"])
async def start_handler(message: types.Message):
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name
    user_name = message.from_user.first_name

    await message.reply(f"Привет, {user_name}")
    await ask(message)


@dp.callback_query_handler(text=["yes", "no"])
async def answer(call: types.CallbackQuery):
    if call.data == "yes":
        await call.message.answer("Красава")
    if call.data == "no":
        await call.message.answer("Ебать ты лох!")
    await call.answer()


if __name__ == '__main__':
    executor.start_polling(dp)
