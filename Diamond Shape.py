


n = int(input("Enter an odd number: "))

if n % 2 == 0:
    print("Please provide an odd integer.")
else:
    # Top half of the diamond
    for i in range(n // 2 + 1):
        print(' ' * (n // 2 - i) + '*' * (2 * i + 1))

    # Bottom half of the diamond
    for i in range(n // 2 - 1, -1, -1):
        print(' ' * (n // 2 - i) + '*' * (2 * i + 1))
