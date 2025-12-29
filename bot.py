import asyncio
import logging
from datetime import datetime
import pytz

from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.client.session.aiohttp import AiohttpSession  # PROXY UCHUN

# --- SOZLAMALAR ---
TOKEN = "8268428884:AAFTFQX6WHDgAaPOjH4tl6yGJsL40Xn0FoM"
CHANNEL_ID = -1002486497988 
CHANNEL_URL = "https://t.me/omadlisoqqa"

# SIZNING SHAXSIY LINKLARINGIZ
MELBET_LINK = "https://refpa3665.com/L?tag=d_4848779m_61049c_betgouz&site=4848779&ad=61049&r=registration"
STARZ_LINK = "https://top100bonus.com/L?tag=d_4866577m_98890c_&site=4866577&ad=98890"
LINEBET_LINK = "https://top100bonus.com/L?tag=d_4866577m_98890c_&site=4866577&ad=98890"

logging.basicConfig(level=logging.INFO)

# --- PYTHONANYWHERE UCHUN PROXY SOZLAMASI ---
# Tekin akkauntlarda Telegramga faqat proxy orqali chiqish mumkin
session = AiohttpSession(proxy="http://proxy.server:3128")
bot = Bot(token=TOKEN, session=session)
dp = Dispatcher()
TASHKENT_TZ = pytz.timezone('Asia/Tashkent')

# --- ASOSIY MENYU ---
def get_main_menu():
    now = datetime.now(TASHKENT_TZ).strftime("%H:%M")
    kb = [
        [KeyboardButton(text="💣 Mines Strategiyasi"), KeyboardButton(text="✈️ Aviator Signal")],
        [KeyboardButton(text="⚽️ Futbol Bashoratlar"), KeyboardButton(text="💰 Maxsus Bonus")],
        [KeyboardButton(text=f"⏰ Yangilash (Toshkent: {now})")]
    ]
    return ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)

# --- OBUNA TEKSHIRISH ---
async def check_sub_channel(user_id):
    try:
        member = await bot.get_chat_member(chat_id=CHANNEL_ID, user_id=user_id)
        return member.status in ['creator', 'administrator', 'member']
    except:
        return False

# --- START ---
@dp.message(Command("start"))
async def start_command(message: types.Message):
    is_sub = await check_sub_channel(message.from_user.id)
    if is_sub:
        await message.answer(
            f"🌟 **PROFESSIONAL ANALITIKA BOTI**\n\n"
            f"Assalomu alaykum, {message.from_user.first_name}!\n"
            f"Botimiz orqali eng aniq strategiyalarni oling va yutishni boshlang.",
            reply_markup=get_main_menu()
        )
    else:
        kb = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="Kanalga a'zo bo'lish ➕", url=CHANNEL_URL)],
            [InlineKeyboardButton(text="Tekshirish ✅", callback_data="check_sub")]
        ])
        await message.answer("🛑 **DIQQAT!** Botdan foydalanish uchun kanalga a'zo bo'ling:", reply_markup=kb)

# --- MINES ---
@dp.message(F.text == "💣 Mines Strategiyasi")
async def mines_handler(message: types.Message):
    text = (
        "💣 **MINES PRO TAKTIKA (V.2025)**\n\n"
        "Ushbu taktika faqat **888STARZ** yangi akkauntlarida 95% aniqlikda ishlaydi:\n\n"
        "1️⃣ Pastdagi havola orqali ro'yxatdan o'ting.\n"
        "2️⃣ 3 ta bomba rejimini tanlang.\n"
        "3️⃣ Kataklarni 'X' shaklida oching."
    )
    kb = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="💎 888STARZ-da sinab ko'rish", url=STARZ_LINK)]])
    await message.answer(text, reply_markup=kb)

# --- AVIATOR ---
@dp.message(F.text == "✈️ Aviator Signal")
async def aviator_handler(message: types.Message):
    text = (
        "✈️ **AVIATOR LIVE SIGNAL**\n\n"
        "Hozirda **MELBET** algoritmi 1.6x dan 2.5x gacha ishlamoqda.\n\n"
        "🔹 **Qoida:** Faqat yangi ro'yxatdan o'tganlar uchun algoritm ochiq."
    )
    kb = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="🚀 MELBET-da boshlash", url=MELBET_LINK)]])
    await message.answer(text, reply_markup=kb)

# --- FUTBOL ---
@dp.message(F.text == "⚽️ Futbol Bashoratlar")
async def soccer_handler(message: types.Message):
    now = datetime.now(TASHKENT_TZ).strftime("%d.%m.%Y")
    text = f"⚽️ **KUNLIK TAHLIL ({now})**\n\n✅ **G'alaba (W1)** — Ishonch: 88%"
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🏆 LINEBET-da tikish", url=LINEBET_LINK)],
        [InlineKeyboardButton(text="🏆 888STARZ-da tikish", url=STARZ_LINK)]
    ])
    await message.answer(text, reply_markup=kb)

# --- BONUS ---
@dp.message(F.text == "💰 Maxsus Bonus")
async def bonus_handler(message: types.Message):
    text = "🎁 **MAXSUS BONUSLAR:**\n\nMelbet va 888Starz uchun 200% gacha bonus!"
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🎁 MELBET BONUS", url=MELBET_LINK)],
        [InlineKeyboardButton(text="🎁 888STARZ BONUS", url=STARZ_LINK)]
    ])
    await message.answer(text, reply_markup=kb)

# --- YANGILASH ---
@dp.message(F.text.contains("Yangilash"))
async def refresh_handler(message: types.Message):
    await message.answer("Barcha koeffitsientlar va vaqt yangilandi! ✅", reply_markup=get_main_menu())

async def main():
    print("--- Bot PythonAnywhere-da ishga tushdi ---")
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())