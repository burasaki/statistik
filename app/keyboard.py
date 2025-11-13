from aiogram.types import (ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup)
from aiogram.utils.keyboard import InlineKeyboardBuilder
from rating import grops_predmets_info


grops = [x for x in grops_predmets_info]

async def inline_grops():
    keyboard = InlineKeyboardBuilder()
    for grop in grops:
        keyboard.add(InlineKeyboardButton(text=grop, callback_data=grop))
    return keyboard.adjust(2).as_markup()


async def inline_studenst(students_rating):
    students = [x for x in students_rating]

    keyboard = InlineKeyboardBuilder()
    for student in students:
        keyboard.add(InlineKeyboardButton(text=student, callback_data=f'name_{student}'))
    keyboard.add(InlineKeyboardButton(text="К выбору группы", callback_data=f'main'))
    return keyboard.adjust(1).as_markup()

main = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="К выбору группы", callback_data='main')]
    ])