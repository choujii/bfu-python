import xml.etree.ElementTree as ET

# Загрузка исходного XML-файла
tree = ET.parse('ex_2.xml')
root = tree.getroot()

# Создание нового элемента Item
new_item = ET.Element("Item")
ET.SubElement(new_item, "ArtName").text = "Сыр Чеддер"
ET.SubElement(new_item, "Barcode").text = "2000000000150"
ET.SubElement(new_item, "QNT").text = "150.00"
ET.SubElement(new_item, "QNTPack").text = "150.00"
ET.SubElement(new_item, "Unit").text = "шт"
ET.SubElement(new_item, "SN1").text = "00000012"
ET.SubElement(new_item, "SN2").text = "05.04.2020"
ET.SubElement(new_item, "QNTRows").text = "12"

# Добавление нового элемента Item в секцию Detail
detail = root.find("Detail")
detail.append(new_item)

# Пересчет значений в Summary
total_summ = 0.0
total_summ_rows = 0

for item in detail.findall("Item"):
    total_summ += float(item.find("QNT").text.replace(",", "."))
    total_summ_rows += int(item.find("QNTRows").text)

# Обновление значений в Summary
summary = root.find("Summary")
summary.find("Summ").text = f"{total_summ:.2f}"
summary.find("SummRows").text = str(total_summ_rows)

# Сохранение нового XML-файла
tree.write("updated_ex_2.xml", encoding="UTF-8", xml_declaration=True)
