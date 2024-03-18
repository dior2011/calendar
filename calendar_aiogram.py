import aiogram
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart,Command
from aiogram import F
from aiogram.types import Message
from aiogram import types
import asyncio
import logging
import sys
from aiogram.fsm.context import FSMContext
from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import ContentType, File, Message
import calendar

TOKEN = "6796185877:AAE7DFikiOA-RW2YvKTnExVHuYqcMVPEAwc"
dp = Dispatcher()
bot = Bot(TOKEN, parse_mode=ParseMode.HTML)

@dp.message(CommandStart())
async def start_command(message:Message):
    await message.answer(text="Qaysi yilning kalendarini ko'rmoqchisiz?")
from aiogram.types import FSInputFile
@dp.message(F.text)
async def kalendar_yuborish(message: Message,state:FSMContext):
    try:
        yil = int(message.text)
        with open(f"kalendar{yil}.txt", mode="x") as kalendar:
            kalendar.write(calendar.calendar(yil))
        file = FSInputFile(f"kalendar{yil}.txt")
        await message.answer_document(document=file)
        
    except:
        await message.answer(text="Iltimos, faqat yil kiriting!")
            



    
    
async def main() -> None:
    global bot
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())

