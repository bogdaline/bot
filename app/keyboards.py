from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

main = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Reminder')],
        [KeyboardButton(text='Weather')]
    ], 
    resize_keyboard=True, 
    input_field_placeholder="Choose"
)

weather_inline = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Weather in Moscow', callback_data='weather')]
])