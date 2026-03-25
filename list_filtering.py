numbers = [3, 6, 9, 12, 15, 18]

result  = list(filter(lambda num:  num % 3 == 0 and num > 10, numbers))
print(result)



