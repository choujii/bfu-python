from PIL import Image

# Открытие изображения
image = Image.open("lab_2.jpg")

# Разделение на каналы R, G, B
r, g, b = image.split()

# Показ оригинального изображения и отдельных каналов
image.show(title="Original Image")
r.show(title="Red Channel")
g.show(title="Green Channel")
b.show(title="Blue Channel")
