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

with open('products1.json', 'w') as f:
    print("Python object is converting into a JSON File using DUMP")
    json.dump(product_data, f)

string = json.dumps(product_data)

with open('products2.json', 'w') as f:
    print("Python object is converting into a JSON string file using DUMPS")
    f.write(string)

with open('products1.json', 'r') as f:
    data1 = json.load(f)
    print("\nLoaded from products1.json:")
    print(data1)
    print(type(data1))

with open('products2.json', 'r') as f:
    data2 = f.read()
    print("\nLoaded from products2.json:")
    print(data2)
    print(type(data2))
