from pathlib import Path


def create_missing_files(missing_file_list, target_dir):
    """
    Читает список отсутствующих файлов из файла и создает их в указанной директории.

    :param missing_file_list: Путь к файлу, содержащему список отсутствующих файлов
    :param target_dir: Путь к директории, в которой будут создаваться отсутствующие файлы
    """
    target_path = Path(target_dir)
    target_path.mkdir(exist_ok=True)  # Создаем директорию, если она не существует

    # Чтение списка отсутствующих файлов и создание их в целевой директории
    with open(missing_file_list, 'r') as file_list:
        for line in file_list:
            file_name = line.strip()  # Читаем имя файла, удаляя пробельные символы
            (target_path / file_name).touch()  # Создаем пустой файл


if __name__ == "__main__":
    import sys

    # Проверяем количество аргументов
    if len(sys.argv) != 3:
        print("Usage: python script.py <missing_file_list> <target_directory>")
    else:
        create_missing_files(sys.argv[1], sys.argv[2])
