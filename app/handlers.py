from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery

import app.keyboard as kb
import rating

router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(f'Выберите группу', reply_markup=await kb.inline_grops())

@router.callback_query(F.data == "main")
async def cmd_start(callback: CallbackQuery):
    await callback.message.edit_text(f'Выберите группу', reply_markup=await kb.inline_grops())


@router.callback_query(F.data.startswith('ИКС'))
async def get_grop_ratings(callback: CallbackQuery):
    global students_rating
    students_rating = rating.get_ratings_all_students(callback.data)
    await callback.answer(f'')
    await callback.message.edit_text("Выберите фамилию", reply_markup= await kb.inline_studenst(students_rating))


@router.callback_query(F.data.startswith('name_'))
async def get_student_rating(callback: CallbackQuery):
    name = callback.data.split('_')[1]
    await callback.answer(f'')
    await callback.message.edit_text(f'{name}\n' +"\n".join(f"{key}: {value}" for key, value in students_rating[name].items()),
                                     reply_markup=kb.main)