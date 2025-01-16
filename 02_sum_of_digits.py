n = int(input("Enter the number to sum: "))

def sum_of_digits(n):
    initial = 0
    while n > 0:
        temp = n % 10
        initial += temp
        n = n // 10
    return initial


print_sum = sum_of_digits(n)
print(print_sum)

# method 2

number = int(input("number: "))
digit_sum = 0
for i in str(number):
    digit_sum += int(i)

print("sum: ", digit_sum)
