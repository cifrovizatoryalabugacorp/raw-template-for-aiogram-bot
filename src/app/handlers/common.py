# from typing import Union

from aiogram import types
from aiogram import Router
# from aiogram.filters import Command
# from aiogram.fsm.context import FSMContext

from app.create_sub_processes import BotDB
from app.keyboards import start_kb


router = Router()


@router.message(Command("start"))
async def cmd_start(message: types.Message):  # , state: FSMContext):
    user = message.from_user.id  # type: ignore[union-attr]

    # current_state = await state.get_state()
    # if current_state is not None:
    #     await state.clear()

    if BotDB.user_exists(user):
        await message.answer("Проверка условия регистрации")
        return

    await message.answer(
        "Тестовое сообщение", reply_markup=start_kb())
