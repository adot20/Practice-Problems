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