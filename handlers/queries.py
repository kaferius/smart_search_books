from aiogram import Router, F
from aiogram.filters import Command, StateFilter
from aiogram import types
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State

from . import message_texts as MT

router = Router()

class Queries(StatesGroup):
    describe = State()

@router.message(Command("ask"), StateFilter(None))
async def ask(message : types.Message, state : FSMContext):
    await message.answer(MT.ask_text)
    await state.set_state(Queries.describe)



@router.callback_query(F.data == "ask", StateFilter(None))
async def ask_button(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.answer(MT.ask_text)
    await state.set_state(Queries.describe)
    await callback.answer()


@router.message(F.text, StateFilter(Queries.describe))
async def query(message : types.Message, state : FSMContext):
    await message.answer("вот ответ")
    await state.clear()