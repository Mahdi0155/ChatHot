from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.contrib.fsm_storage.memory import MemoryStorage

API_TOKEN = '8058462987:AAF118uJ5cZ9K-38Wp5uNjGyTL9fb30T6so'

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())

admin_id = 6387942633

user_menu = ReplyKeyboardMarkup(resize_keyboard=True)
user_menu.add(KeyboardButton("استارت چت"))
user_menu.add(KeyboardButton("ایجاد پروفایل"), KeyboardButton("مشاهده پروفایل"))
user_menu.add(KeyboardButton("دعوت دوستان"), KeyboardButton("درخواست اسپانسر شدن"))

admin_menu = ReplyKeyboardMarkup(resize_keyboard=True)
admin_menu.add(
    KeyboardButton("مدیریت پیام‌های رندوم"),
    KeyboardButton("مدیریت پروفایل‌های رندوم"),
)
admin_menu.add(
    KeyboardButton("مدیریت عضویت‌های اجباری"),
    KeyboardButton("مدیریت ادمین‌ها"),
)
admin_menu.add(
    KeyboardButton("مشاهده آمار"),
    KeyboardButton("ارسال پیام همگانی"),
)

@dp.message_handler(commands=['start'])
async def start_cmd(message: types.Message):
    if message.from_user.id == admin_id:
        await message.answer("خوش آمدید ادمین محترم.", reply_markup=user_menu)
    else:
        await message.answer("خوش آمدید به ربات.", reply_markup=user_menu)

@dp.message_handler(commands=['پنل'])
async def admin_panel(message: types.Message):
    if message.from_user.id == admin_id:
        await message.answer("وارد پنل مدیریت شدید.", reply_markup=admin_menu)

@dp.message_handler(lambda message: True)
async def handle_buttons(message: types.Message):
    if message.text in [
        "مدیریت پیام‌های رندوم",
        "مدیریت پروفایل‌های رندوم",
        "مدیریت عضویت‌های اجباری",
        "مدیریت ادمین‌ها",
        "مشاهده آمار",
        "ارسال پیام همگانی",
    ]:
        await message.reply("این بخش هنوز طراحی نشده.")
    elif message.text in [
        "استارت چت",
        "ایجاد پروفایل",
        "مشاهده پروفایل",
        "دعوت دوستان",
        "درخواست اسپانسر شدن",
    ]:
        await message.reply("این بخش هنوز طراحی نشده.")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
