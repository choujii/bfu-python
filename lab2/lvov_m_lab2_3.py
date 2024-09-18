from PIL import Image, ImageDraw, ImageFont

image = Image.open("lab_2.jpg").convert("RGBA")
watermark = Image.open("watermark.png")
if watermark.mode != 'RGBA':
    watermark = watermark.convert("RGBA")

# Создание объекта для рисования на изображении
draw = ImageDraw.Draw(image)
# Загрузка шрифта по умолчанию, который будет использоваться для текста водяного знака
font = ImageFont.load_default()

# Текст водяного знака, который будет нанесен на изображение
text = "Lvov M."

# Получение габаритов текста (ширина и высота) с помощью метода textbbox()
# Это необходимо для того, чтобы точно позиционировать текст на изображении
bbox = draw.textbbox((0, 0), text, font=font)
text_width, text_height = bbox[2] - bbox[0], bbox[3] - bbox[1]


width, height = image.size

position = (width - text_width - 10, height - text_height - 10)

draw.text(position, text, font=font, fill=(255, 255, 255, 128))

# Получение размеров изображения водяного знака (ширина и высота)
watermark_width, watermark_height = watermark.size

# Определение максимальных размеров водяного знака (1/10 от размера основного изображения)
max_width, max_height = width // 10, height // 10

# Если водяной знак больше установленных ограничений, изменяем его размер пропорционально
if watermark_width > max_width or watermark_height > max_height:
    watermark.thumbnail((max_width, max_height))

watermark_position = (10, 10)
image.alpha_composite(watermark, dest=watermark_position)
image.show()
image = image.convert("RGB")
image.save("watermarked_image.jpg")
