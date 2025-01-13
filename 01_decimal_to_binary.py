# change decimal number to binary
# example: 10 - 1010

number = int(input())

def decimal_to_binary(number):
    if number == 0:
        return "0"
    binary = ""
    while number > 0:
        remainder = number % 2
        binary = str(remainder) + binary
        number = number // 2
    return binary

binary_result = decimal_to_binary(number)
print(binary_result)