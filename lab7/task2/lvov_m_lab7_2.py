import json

# Исходный файл и файл для форматирования
input_file = "ex_2.json"
formatted_file = "ex_2_formatted.json"

# Чтение и форматирование файла
with open(input_file, "r") as file:
    data = json.loads(f"[{file.read()}]")  # Добавляем [] для корректного чтения как список

# Сохранение в читабельном виде
with open(formatted_file, "w") as file:
    json.dump(data, file, indent=4)
print(f"Читабельный файл сохранен в {formatted_file}")

# Извлечение имен пользователей и телефонов
users_dict = {user["name"]: user["phoneNumber"] for user in data}

# Вывод на экран
print("\nИзвлеченные данные:")
print(users_dict)
