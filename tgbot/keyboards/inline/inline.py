from aiogram.dispatcher.filters.callback_data import CallbackData
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

# Example
# def proceed() -> InlineKeyboardMarkup:
#     keyboard = InlineKeyboardBuilder()
#     keyboard.add(
#         InlineKeyboardButton(text='Продолжить >>', callback_data='proceed')
#     )
#     keyboard.adjust(1, repeat=True)
#     return keyboard.as_markup()
