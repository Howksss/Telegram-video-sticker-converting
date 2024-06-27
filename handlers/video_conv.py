from aiogram import  types, F, Router, Bot
from apple import converting as cov
from aiogram.types import FSInputFile
import os
from dotenv import load_dotenv


router = Router()
load_dotenv()
bot = Bot(os.getenv('TOKEN'))

@router.message(F.video)
async def download_video(message: types.Video):
    if int(message.video.duration) > 3:
        await message.reply('Видео слишком длинное!')
    elif int(message.video.file_size) > 1048576:
        await message.reply('Видео весит слишком много!')
    else:
        filik_id = message.video.file_id
        try:
            await bot.download(
                message.video,
                destination=fr'C:\Users\*someuser*\PycharmProjects\BOT_AIO_1\{filik_id}.mp4'
            )
            await message.reply('Видеоролик успешно загружен! Ожидайте конвертации')
        except Exception:
            await message.answer('Видеоролик не удалось загрузить')
        try:
            cov.convert(message.video.file_id)
            await message.reply('Конвертация прошла успешно!')
        except Exception:
            await message.answer('Конвертация не удалась')
        try:
            document = FSInputFile(path=fr'C:\Users\*someuser*\PycharmProjects\BOT_AIO_1\{filik_id}.webm')
            await bot.send_video(message.chat.id, document, caption='Ваш файл🥰:')
        except Exception:
            await message.answer('Не удалось отправить видеоролик')
        cov.cleaning(filik_id)