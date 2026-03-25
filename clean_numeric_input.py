values = ["100", "200", "NaN", "50", "error", "300"]

def clean_inputs(input_list):
    cleaned_list = []
    for item in input_list:
        try:
            number = int(item)
            cleaned_list.append(number)
        except ValueError:
            continue
    return cleaned_list

result = clean_inputs(values)
print(result)







