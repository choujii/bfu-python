from PIL import Image, ImageDraw, ImageFont

# Функция для создания карточки с цифрой
def create_card(number, filename):
    # Создание изображения размером 100x100 с белым фоном
    image = Image.new("RGB", (100, 100), "white")
    draw = ImageDraw.Draw(image)

    # Рисование синей рамки толщиной 5 пикселей
    draw.rectangle([(5, 5), (95, 95)], outline="blue", width=5)

    # Настройка шрифта и цвета текста
    font = ImageFont.load_default()  # Использование шрифта по умолчанию
    text = str(number)  # Цифра для вывода

    # Получение размеров текста для его центрирования
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width, text_height = bbox[2] - bbox[0], bbox[3] - bbox[1]
    text_position = ((100 - text_width) // 2, (100 - text_height) // 2)

    # Рисование красной цифры в центре изображения
    draw.text(text_position, text, font=font, fill="red")

    # Сохранение изображения в формате PNG
    image.save(filename)

    # Показ изображения
    image.show()

create_card(1, "lab_2_4_1.png")
create_card(2, "lab_2_4_2.png")
create_card(3, "lab_2_4_3.png")
