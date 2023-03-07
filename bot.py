import time
import logging

from aiogram import Bot, Dispatcher, executor, types

TOKEN = "5674619352:AAEDay5rCaj6hfWp6lgyDPJiJYrj0uSFR5A"

bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot)


@dp.message_handler(commands=["start"])
async def start_handler(message: types.Message):
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name
    user_name = message.from_user.first_name

    await message.reply(f"Hi, {user_name}")

    for i in range(10):
        time.sleep(2)

        await bot.send_message(user_id, f"Всё ещё лох, {user_name}?")


if __name__ == '__main__':
    executor.start_polling(dp)
