class InvalidWeightError(Exception):
    pass

def validate_weight(weight):
    if weight <= 0 or weight > 500:
        raise InvalidWeightError(f"Invalid Weight: {weight}. Must be between 1 and 500")
    else:
        return "Valid Weight"
    

try:
    print(validate_weight(150))
    print(validate_weight(600))
except InvalidWeightError as e:
    print(e)




    
