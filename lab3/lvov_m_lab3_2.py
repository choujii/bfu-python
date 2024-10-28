from PIL import Image
import matplotlib.pyplot as plt
from skimage import io
import numpy as np


# Функция для построения гистограммы изображения
def plot_histogram(image):
    plt.figure(figsize=(10, 4))
    plt.hist(image.ravel(), bins=256, color='gray', alpha=0.5)
    plt.title("Гистограмма изображения")
    plt.xlabel("Яркость")
    plt.ylabel("Частота")
    plt.show()


# Функция для построения гистограмм каждого канала (R, G, B)
def plot_rgb_histograms(image):
    # Разделяем каналы
    red_channel = image[:, :, 0]
    green_channel = image[:, :, 1]
    blue_channel = image[:, :, 2]

    # Построение гистограмм для каждого канала
    plt.figure(figsize=(15, 4))

    plt.subplot(1, 3, 1)
    plt.hist(red_channel.ravel(), bins=256, color='red', alpha=0.5)
    plt.title("Гистограмма R канала")
    plt.xlabel("Яркость")
    plt.ylabel("Частота")

    plt.subplot(1, 3, 2)
    plt.hist(green_channel.ravel(), bins=256, color='green', alpha=0.5)
    plt.title("Гистограмма G канала")
    plt.xlabel("Яркость")
    plt.ylabel("Частота")

    plt.subplot(1, 3, 3)
    plt.hist(blue_channel.ravel(), bins=256, color='blue', alpha=0.5)
    plt.title("Гистограмма B канала")
    plt.xlabel("Яркость")
    plt.ylabel("Частота")

    plt.tight_layout()
    plt.show()


image_path = "original_photo.jpg"
image = Image.open(image_path)
image_np = np.array(image)

# Отображение исходного изображения
plt.figure(figsize=(5, 5))
plt.imshow(image)
plt.axis("off")
plt.title("Исходное изображение")
plt.show()

# Построение общей гистограммы изображения
plot_histogram(image_np)

# Построение гистограмм для каждого из каналов R, G, B
plot_rgb_histograms(image_np)
