from aiogram.utils.keyboard import (
    ReplyKeyboardBuilder,
    InlineKeyboardBuilder
)
from aiogram.types import InlineKeyboardButton, KeyboardButton


def start_kb():
    builder = ReplyKeyboardBuilder()
    builder.row(
        KeyboardButton(text="Начать")
    )
    return builder.as_markup(resize_keyboard=True)
