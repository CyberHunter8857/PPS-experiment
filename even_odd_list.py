def even_odd(numbers):
    even = []
    odd = []
    for num in numbers:
        if num % 2 == 0:
            even.append(num)
        else:
            odd.append(num)
    return even, odd

n = int(input("Enter the number of integers: "))
numbers = []
for i in range(n):
    num = int(input("Enter an integer: "))
    numbers.append(num)

even_list, odd_list = even_odd(numbers)

print("Your List:", numbers)
print("Even numbers:", even_list)
print("Odd numbers:", odd_list)