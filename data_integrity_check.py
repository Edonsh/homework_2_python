products = [
    {"id": 1, "name": "Table", "price": 200},
    {"id": 2, "name": "", "price": 150},
    {"id": 3, "name": "Chair", "price": -50},
    {"id": None, "name": "Lamp", "price": 80}
]

def validate_products(input_products):
    invalid_products = []
    for prod in input_products:
        if prod["id"] == None:
            invalid_products.append({
                "product": prod,
                "reason": "Id must not be None"
            })
        elif prod["name"] == "":
            invalid_products.append({
                "product": prod,
                "reason": "Name must not be empty"
            })
        elif prod["price"] < 0:
            invalid_products.append({
                "product": prod,
                "reason": "Price must be positive"
            })
        else:
            continue
    return invalid_products

result = validate_products(products)
for prod in result:
    print(prod)
    
    