import xml.etree.ElementTree as ET

tree = ET.parse('ex_3.xml')
root = tree.getroot()

# Поиск и вывод данных о товарах
print("Список товаров в счет-фактуре:")
for item in root.findall(".//ТаблСчФакт/СведТов"):
    # Извлечение информации о товаре
    name = item.get("НаимТов")
    quantity = item.get("КолТов")
    price = item.get("ЦенаТов")
    print(f"Товар: {name}, Количество: {quantity}, Цена: {price}")
