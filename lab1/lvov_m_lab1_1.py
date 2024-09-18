import os
from pathlib import Path
import shutil


def scan_and_copy(directory): #Сканирует указанную директорию на наличие файлов размером меньше 2К и копирует их в папку 'small'
    # Если путь не задан, используем текущую рабочую директорию
    dir_path = Path(directory) if directory else Path.cwd()

    # Находим все файлы размером меньше 2К (2048 байт)
    small_files = [f for f in dir_path.glob('*') if f.is_file() and f.stat().st_size < 2048]

    # Если найдены файлы, создаем папку 'small' и копируем в нее файлы
    if small_files:
        small_folder = dir_path / 'small'
        small_folder.mkdir(exist_ok=True)  # Создаем папку, если она не существует

        for file in small_files:
            shutil.copy(file, small_folder / file.name)  # Копируем файл в папку 'small'

        print("Small files found and copied:")
        for file in small_files:
            print(file.name)
    else:
        print("No small files found.")


if __name__ == "__main__":
    import sys

    # Если передан аргумент, используем его как путь к директории, иначе сканируем текущую директорию
    if len(sys.argv) > 1:
        scan_and_copy(sys.argv[1])
    else:
        scan_and_copy(None)
