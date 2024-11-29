import sqlite3

# Создаем базу данных SQLite
db_path = "delivery_service.db"
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Создаем таблицы "Курьер" и "Транспорт" из схемы
cursor.execute("""
CREATE TABLE Courier (
    courier_id INTEGER PRIMARY KEY,
    last_name TEXT NOT NULL,
    first_name TEXT NOT NULL,
    middle_name TEXT,
    passport_number TEXT,
    birth_date DATE,
    hire_date DATE,
    work_start_time TIME,
    work_end_time TIME,
    city TEXT,
    street TEXT,
    house INTEGER,
    apartment INTEGER,
    phone TEXT
);
""")

cursor.execute("""
CREATE TABLE Transport (
    vehicle_id INTEGER PRIMARY KEY,
    brand TEXT NOT NULL,
    registration_date DATE,
    color TEXT
);
""")

# Добавляем строку в таблицу "Курьер"
cursor.execute("""
INSERT INTO Courier (last_name, first_name, middle_name, passport_number, birth_date, hire_date,
                     work_start_time, work_end_time, city, street, house, apartment, phone)
VALUES ('Иванов', 'Иван', 'Иванович', '1234567890', '1990-01-01', '2020-05-01',
        '09:00', '18:00', 'Москва', 'Ленина', 10, 5, '+79998887766');
""")

# Добавляем строку в таблицу "Транспорт"
cursor.execute("""
INSERT INTO Transport (brand, registration_date, color)
VALUES ('Ford', '2022-01-15', 'Белый');
""")

# Изменяем данные в таблице "Курьер" (изменяем рабочие часы)
cursor.execute("""
UPDATE Courier
SET work_start_time = '08:00', work_end_time = '17:00'
WHERE last_name = 'Иванов';
""")

# Сохраняем изменения и закрываем соединение
conn.commit()
conn.close()
