import os
import numpy as np
from moviepy.video.io.VideoFileClip import VideoFileClip
from PIL import Image


def extract_frames(input_file, start_time, end_time, output_folder, step=10):
    try:
        # Создаем выходную папку, если она не существует
        os.makedirs(output_folder, exist_ok=True)

        with VideoFileClip(input_file) as video:
            # Проверка на корректность временных параметров
            if start_time < 0 or end_time > video.duration or start_time >= end_time:
                print("Ошибка: Проверьте время начала и окончания.")
                return

            # Извлекаем кадры с заданным шагом
            for t in range(int(start_time), int(end_time), step):
                frame = video.get_frame(t)
                # Изменяем размер кадра до ширины 250, сохраняя пропорции
                frame_resized = resize_frame(frame, width=250)

                # Сохраняем кадр как изображение
                frame_file = os.path.join(output_folder, f"frame_{t}.png")
                Image.fromarray(frame_resized).save(frame_file)
                print(f"Сохранен кадр: {frame_file}")

    except Exception as e:
        print(f"Произошла ошибка: {e}")


def resize_frame(frame, width):
    # Получаем исходные размеры
    original_height, original_width, _ = frame.shape
    height = int((width / original_width) * original_height)

    # Изменяем размер с использованием PIL
    img = Image.fromarray(frame)
    img_resized = img.resize((width, height))
    return np.array(img_resized)


if __name__ == "__main__":
    input_file = "input_video.mp4"
    start_time = 1
    end_time = 30
    output_folder = "extracted_frames"
    step = 10

    extract_frames(input_file, start_time, end_time, output_folder, step)
