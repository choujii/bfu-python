import sys
import argparse
from pathlib import Path


def process_files(dirpath, files):
    dir_path = Path(dirpath)

    # Проверяем, существует ли директория
    if not dir_path.is_dir():
        print(f"The directory {dirpath} does not exist.")
        return

    existing_files = []
    missing_files = []

    # Проверяем наличие каждого файла в директории
    for file in files:
        file_path = dir_path / file
        if file_path.is_file():
            existing_files.append(file)  # Файл существует
        else:
            missing_files.append(file)  # Файл отсутствует

    # Выводим и сохраняем список существующих файлов
    if existing_files:
        print("Existing files:")
        print('\n'.join(existing_files))
        with open('existing_files.txt', 'w') as f:
            f.write('\n'.join(existing_files))
    else:
        print("No files exist.")

    # Выводим и сохраняем список отсутствующих файлов
    if missing_files:
        print("Missing files:")
        print('\n'.join(missing_files))
        with open('missing_files.txt', 'w') as f:
            f.write('\n'.join(missing_files))
    else:
        print("All files are present.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--dirpath', default='.', help='Directory path')
    parser.add_argument('--files', nargs='*', help='List of files to check', default=[])
    args = parser.parse_args()

    process_files(args.dirpath, args.files)

