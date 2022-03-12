from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder

# Example
# def rcancel() -> ReplyKeyboardMarkup:
#     keyboard = ReplyKeyboardBuilder().row(
#         KeyboardButton(text='Отмена'),
#         KeyboardButton(text='Ок'),
#     )
#
#     keyboard.adjust(1, repeat=True)
#     return keyboard.as_markup(resize_keyboard=True)
