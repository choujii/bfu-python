from PIL import Image
import sys  # модуль для работы с аргументами командной строки
# Получаем путь к изображению из аргументов командной строки
# sys.argv[1] содержит первый аргумент, который передается при запуске программы
image_path = sys.argv[1]

with Image.open(image_path) as img:
    img = img.convert('RGB')  # Преобразуем изображение в RGB-формат
    pixels = img.getdata()  # Получаем данные о каждом пикселе изображения
# Инициализируем переменные для подсчета суммы значений каналов R, G и B
red_total = 0
green_total = 0
blue_total = 0
# Проходим по каждому пикселю изображения (каждый пиксель представлен кортежем из 3 значений: R, G, B)
for pixel in pixels:
    red_total += pixel[0]
    green_total += pixel[1]
    blue_total += pixel[2]

if red_total > green_total and red_total > blue_total:
    dominant_color = 'Red'
elif green_total > red_total and green_total > blue_total:
    dominant_color = 'Green'
else:
    dominant_color = 'Blue'  # Синий цвет преобладает

# Выводим результат с информацией о том, какой цвет преобладает
print(f"The dominant color is {dominant_color}")

# Запуск программы через терминал осуществляется командой "python main.py lab_2.jpg"
