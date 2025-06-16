from aiogram import Router, types, F
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State

from . import message_texts as MT

import CONFIG

class Support(StatesGroup):
    describe = State()


router = Router()

@router.message(Command("support"), StateFilter(None))
async def support(message : types.Message, state: FSMContext):
    await message.answer(MT.support_text)
    await state.set_state(Support.describe)


@router.callback_query(F.data == "support", StateFilter(None))
async def support_button(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.answer(MT.support_text)
    await state.set_state(Support.describe)
    await callback.answer()


@router.message(F.text, StateFilter(Support.describe))
async def problem_description(message : types.Message, state: FSMContext):
    await message.answer(MT.support_answer)
    await message.bot.send_message(
        CONFIG.admin_id,
        text=f"Сообщение от @{message.from_user.username} ({message.from_user.id})\n\n{message.text}")
    await state.clear()