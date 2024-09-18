from PIL import Image
import os

def create_thumbnail(file_path, thumbnail_size=(50, 150)):
    try:
        # Открываем изображение с указанным путем
        with Image.open(file_path) as img:
            # Метод thumbnail изменяет размер изображения, сохраняя его пропорции
            img.thumbnail(thumbnail_size)
            base, ext = os.path.splitext(file_path)
            thumbnail_path = f"{base}_sketch{ext}"

            img.save(thumbnail_path)
            return thumbnail_path
    except Exception as e:
        print(f"Ошибка при обработке файла {file_path}: {e}")
        return None


def show_thumbnails(directory):
    for file_name in os.listdir(directory):
        file_path = os.path.join(directory, file_name)
        if os.path.isfile(file_path) and file_path.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
            # Создаем эскиз изображения
            thumbnail_path = create_thumbnail(file_path)
            if thumbnail_path:
                with Image.open(thumbnail_path) as thumbnail_img:
                    thumbnail_img.show()


your_directory_path = 'C:/Users/0potter0/PycharmProjects/python_3pm_admo_lvov'
show_thumbnails(your_directory_path)
