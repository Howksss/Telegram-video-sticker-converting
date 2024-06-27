from aiogram import  types, F, Router
from aiogram.filters.command import Command
from apple import descs

router = Router()


@router.message(Command('start'))
async def cmd_start(message: types.Message):
    await message.answer('Здравствуй! Ты попал к боту, который может переделать твой видеофайл в формат, идеально подходящий для создания видеостикера', input_field_placeholder = 'Что делаем дальше?')

@router.message(Command('help'))
async def faq(message: types.Message):
    await message.answer(f'{descs.How_to_use}', parse_mode='HTML')

@router.message(Command('admin'))
async def owner(message: types.Message):
    await message.answer(f'{descs.Administrator_inf}')

@router.message(Command('convert'))
async def convert_video(message: types.Message):
    await message.answer('Отправь видеофайл прямо в этот диалог!')

@router.message()
async def shlak(message: types.Message):
    await message.reply('Я тебя не понимаю')
