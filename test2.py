from gtts import gTTS
import os

# Текст, который нужно озвучить

def voise(text):


    # Создание объекта gTTS и сохранение аудиофайла
    tts = gTTS(text, lang='ru')
    tts.save("output.mp3")

    # Воспроизведение аудиофайла
    os.system("mpg123 output.mp3")  # Или используйте другую команду воспроизведения для вашей системы

