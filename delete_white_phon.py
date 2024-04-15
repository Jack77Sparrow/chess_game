from PIL import Image

# Открываем изображение
image = Image.open("photos/b_zam.png")

# Преобразуем изображение в режим RGBA (добавляем альфа-канал)
image = image.convert("RGBA")

# Получаем данные изображения в виде массива пикселей
data = image.getdata()

# Создаем новый массив для обработанных пикселей
new_data = []
for item in data:
    # Если пиксель близок к белому цвету (255, 255, 255), делаем его прозрачным
    if item[:3] == (255, 255, 255):
        new_data.append((255, 255, 255, 0))  # Прозрачный пиксель
    else:
        new_data.append(item)

# Обновляем данные изображения
image.putdata(new_data)

# Сохраняем результат
image.save("photos/w_zam.png", "PNG")
