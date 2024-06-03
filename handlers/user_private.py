from aiogram import types, Router, F
from aiogram.filters import Command, CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from krbs.keyboard import start_kb
user_private_router = Router()

class AddFlower(StatesGroup):
    flower = State()
    count = State()


@user_private_router.message(CommandStart())
async def start(message: types.Message, state: FSMContext):
    await message.answer(f'Привет, {message.from_user.first_name}!😙\nЭто бот чтобы подарить своей любимой цветочки!🥰\nВыбери цветы ниже.', reply_markup=start_kb)
    await state.set_state(AddFlower.flower)



@user_private_router.message(F.text == '🌹Розы')
async def rosy(message: types.Message, state: FSMContext):
    await message.answer('Вы выбрали 🌹розы, теперь введите количество цветов')
    await state.update_data(flower='🌹')
    await state.set_state(AddFlower.count)
    

@user_private_router.message(F.text == '🌷Тюльпаны')
async def tulip(message: types.Message, state: FSMContext):
    await message.answer('Вы выбрали 🌷тюльпаны, теперь введите количество цветов')
    await state.update_data(flower='🌷')
    await state.set_state(AddFlower.count)

@user_private_router.message(F.text == '🌼Ромашки')
async def rose(message: types.Message,  state: FSMContext):
    await message.answer('Вы выбрали 🌼ромашки, теперь введите количество цветов')
    await state.update_data(flower='🌼')
    await state.set_state(AddFlower.count)

@user_private_router.message(AddFlower.count, F.text)
async def count(message: types.Message, state: FSMContext):
    if not message.text.isdigit():
        await message.answer('Введите число!')
        return
    elif int(message.text) > 4096:
        await message.answer('Введите число до 4096 (телеграм просто не даст отправить больше 4096 символов😭)')
        return
    elif int(message.text) <= 0:
        await message.answer('Введите число больше нуля')
        return
    num = int(message.text)
    await state.update_data(count=num)
    _ = 0
    t_ = ''
    data = await state.get_data()
    while _ < num:
        t_ += str(data['flower'])
        _ += 1
    await message.answer(t_)
    _ = 0
    t_ = ''

@user_private_router.message(AddFlower.count)
async def error(message: types.Message, state: FSMContext):
    await message.answer('Введите какое нибудь число до 4096')
    return