import json

input_file = "ex_3.json"
output_file = "output.json"


with open(input_file, "r") as file, open(output_file, "w") as result:
    data = json.load(file)

    invoice = {
              "id": 1,
              "total": 100.00,
              "items": []}
    item4 = {
      "name": "item 4",
      "quantity": 10,
      "price": 5.00
    }

    item5 = {
        "name": "item 5",
        "quantity": 8,
        "price": 35.00
    }

    invoice["items"].append(item4)
    invoice["items"].append(item5)

    for item in invoice["items"]:
        invoice["total"] += item["quantity"] * item["price"]

    data["invoices"].append(invoice)

    json.dump(data, result, indent=2)
