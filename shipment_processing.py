shipments = [
    {"shipment_id": 1, "weight": 10, "status": "delivered"},
    {"shipment_id": 2, "weight": -5, "status": "delivered"},
    {"shipment_id": 3, "weight": 8, "status": "pending"},
    {"shipment_id": 4, "weight": 15, "status": "delivered"}
]

def get_valid_shipments(input_shipments):
    valid_shipments = []

    for item in input_shipments:

        weight = item["weight"]
        status = item["status"]

        if weight > 0 and status == "delivered":
            valid_shipments.append(item)
    
    return valid_shipments


result = get_valid_shipments(shipments)
for item in result:
    print(item)


