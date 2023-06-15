number = int(input("Enter a three-digit number: "))

# Extracting the digits
digit1 = number // 100
digit2 = (number // 10) % 10
digit3 = number % 10

# Calculating the Armstrong sum
armstrong_sum = (digit1 ** 3) + (digit2 ** 3) + (digit3 ** 3)

# Checking if it is an Armstrong number
if armstrong_sum == number:
    print(number, "is an Armstrong number.")
else:
    print(number, "is not an Armstrong number.")
