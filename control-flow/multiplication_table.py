number = int(input("Enter a number to see it's multiplication table: "))
for n in range (1, 11):
    result = number * n
    print(f"{number} * {n} = {result}")