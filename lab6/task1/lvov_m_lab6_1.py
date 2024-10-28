import xmlschema

# Загрузка схемы XSD
schema = xmlschema.XMLSchema('schema.xsd')

# Проверка нового файла с пространством имен
try:
    schema.validate('incorrect_ex_1.xml')
    print("XML-файл успешно прошел валидацию.")
except xmlschema.XMLSchemaException as e:
    print("Ошибка валидации XML-файла:", e)
