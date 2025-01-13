# reverse a string or a number

# Method 1

key_input = input("Enter a string or a number: ")

reverse = ""
for i in str(key_input):
    reverse = i + reverse
    result = reverse
    
print(result)

# Method 2: using function


def reverse_me(input_value):
    reverse = ""
    for i in str(input_value):
        reverse = i + reverse
    return reverse
    
input_value = input("Input: ")
result = reverse_me(input_value)
print(result)

# Method 3 - using slicing

def reverse_me(value):
    store = value[::-1]
    return store

value = str(input("Enter a number or a string to reverse"))
result = reverse_me(value)
print(result)
