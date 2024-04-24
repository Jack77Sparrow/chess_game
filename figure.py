import pyaudio
import wave
import speech_recognition as sr

# Устанавливаем параметры записи звука
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CHUNK = 1024
RECORD_SECONDS = 5
WAVE_OUTPUT_FILENAME = "output.wav"

# Создаем объект PyAudio
audio = pyaudio.PyAudio()

# Открываем поток для записи звука с микрофона
stream = audio.open(format=FORMAT, channels=CHANNELS,
                    rate=RATE, input=True,
                    frames_per_buffer=CHUNK)

print("Запис...")

frames = []

# Записываем звук в поток
for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    frames.append(data)

print("Запис завершена.")

# Останавливаем поток и закрываем объект PyAudio
stream.stop_stream()
stream.close()
audio.terminate()

# Сохраняем записанные данные в файл WAV
with wave.open(WAVE_OUTPUT_FILENAME, 'wb') as wf:
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(audio.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))

print("Запис збережено в", WAVE_OUTPUT_FILENAME)

# Создаем объект Recognizer
recognizer = sr.Recognizer()

# Открываем аудиофайл для распознавания
with sr.AudioFile(WAVE_OUTPUT_FILENAME) as source:
    # Слушаем аудиофайл для получения данных
    audio_data = recognizer.record(source)
    
    try:
        # Используем Google Web Speech API для распознавания речи
        text = recognizer.recognize_google(audio_data, language="en-EN")

        print("Ви сказали:", text)
    except sr.UnknownValueError:
        print("мова не розпізнана")
    except sr.RequestError as e:
        print("помилка запроса до сервісу розпізнавання: {0}".format(e))

