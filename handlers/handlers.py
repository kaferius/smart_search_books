from aiogram import Router, types, F
from aiogram.filters import Command
from aiogram.utils.keyboard import InlineKeyboardBuilder

from . import message_texts as MT

router = Router()

@router.message(Command("start"))
async def start(message : types.Message):
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(text="Запрос", callback_data="ask"))
    builder.add(types.InlineKeyboardButton(text="Техподдержка", callback_data="support"))
    builder.add(types.InlineKeyboardButton(text="О проекте", callback_data="about"))
    await message.answer(
        MT.hello_text,
        reply_markup=builder.as_markup()
    )


@router.message(Command("about"))
async def about(message : types.Message):
    await message.answer(MT.about_text)


@router.callback_query(F.data == "about")
async def support_button(callback: types.CallbackQuery):
    await callback.message.answer(MT.about_text)
    await callback.answer()