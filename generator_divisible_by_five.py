def divisible_by_five_generator(n):
    for i in range(n + 1):
        if i % 5 == 0:
            yield i


for num in divisible_by_five_generator(25):
    print(num)


    