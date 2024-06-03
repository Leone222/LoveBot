from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

start_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='🌹Розы'),
        ], 
        {
            KeyboardButton(text='🌷Тюльпаны')
            },
            {
                KeyboardButton(text='🌼Ромашки')
            }
    ],
    resize_keyboard=True

)