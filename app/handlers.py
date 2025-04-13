from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart
import app.keyboards as keyboard
import requests

router = Router()

URL = 'https://api.open-meteo.com/v1/forecast?latitude=55.7558&longitude=37.6173&current=temperature_2m,apparent_temperature,wind_speed_10m,wind_gusts_10m,rain&past_days=1&forecast_days=1'

# /start
@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('Welcome to', reply_markup=keyboard.main)

@router.message(F.text == "Reminder")
async def reminder(message: Message):
    await message.answer("Set your reminder", reply_markup=keyboard.main)

@router.message(F.text == 'Weather')
async def catalog(message: Message):
    await message.answer('Choose the city', reply_markup=keyboard.weather_inline)

@router.callback_query(F.data == 'weather')
async def weather(callback: CallbackQuery):
    response = requests.get(URL)
    
    if response.status_code == 200:
        data = response.json()
        temperature = data.get('current', {}).get('temperature_2m', 'unknown')
        await callback.message.answer(f'The weather in Moscow: {temperature}°C')
    else:
        await callback.answer('Error retrieving weather data', show_alert=True)