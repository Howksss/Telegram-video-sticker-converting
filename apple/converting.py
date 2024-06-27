import os
import subprocess


repr = r'C:\Users\*someuser*\Desktop\ffmpeg-master-latest-win64-gpl\ffmpeg-master-latest-win64-gpl\bin'

def convert(file_name):
    os.rename(fr'C:\Users\*someuser*\PycharmProjects\BOT_AIO_1\{file_name}.mp4', f'{repr}\{file_name}.mp4')
    with open('dada.bat','w') as f:
        f.write(r'cd C:\Users\*someuser*\Desktop\ffmpeg-master-latest-win64-gpl\ffmpeg-master-latest-win64-gpl\bin'+f'\nffmpeg -i {file_name}.mp4 -c:v libvpx-vp9 -vf scale=512:512 -an {file_name}.webm')
    subprocess.call(r'C:\Users\*someuser*\PycharmProjects\BOT_AIO_1\dada.bat')
    os.rename(f'{repr}\{file_name}.webm', fr'C:\Users\*someuser*\PycharmProjects\BOT_AIO_1\{file_name}.webm')

def cleaning(video_id):
    os.remove(fr'C:\Users\*someuser*\Desktop\ffmpeg-master-latest-win64-gpl\ffmpeg-master-latest-win64-gpl\bin\{video_id}.mp4')
    os.remove(fr'C:\Users\*someuser*\PycharmProjects\BOT_AIO_1\{video_id}.webm')