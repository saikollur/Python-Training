import json

product_data = {
    'products' : [
        {"id": 1, "name": "Laptop", "price": 55000},
        {"id": 2, "name": "Mouse", "price": 500},
        {"id": 3, "name": "Keyboard", "price": 1500},
        {"id": 4, "name": "Headphones", "price": 800},
        {"id": 5, "name": "Monitor", "price": 12000}
    ]
}

threshold = 900

with open('productFile.json', 'w') as f:
    json.dump(product_data, f)

with open('productFile.json', 'r') as f:
    newDict = json.load(f)

l = []

for item in newDict["products"]:
    if item["price"] <= threshold:
        l.append(item)

filtered_Data = {}
filtered_Data["products"] = l

with open('filtered_Data.json', 'w') as f:
    json.dump(filtered_Data, f)

with open('filtered_Data.json', 'r') as f:
    data = json.load(f)
    print(data)
    print(type(data))
