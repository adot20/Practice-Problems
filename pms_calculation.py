# Create a calculator that performs arithmetic operations based on user input.
# Input: Two lined input -  A space-separated list of integers (at least two). And, A string of operations ('p', 'm', 's').

# Operations can only be 'p', 'm', or 's'.
# Output:
# Final result if valid; otherwise, "Invalid".

numbers = list(map(int, input("Enter numbers: ").split()))
result = numbers[0]
operations = input("Enter operations: ") # input among pms as in plus/add, multiply, subtract
if len(numbers) != len(operations) + 1:
    print("Invalid")
else:
    valid_operations = {'p', 'm', 's'}
    for op in operations:
        if op not in valid_operations:
            print("Invalid")
            break
    else:
        result = numbers [0]
        #perform operations
        for i in range(len(operations)):
            if operations[i] == 'p':
                result = result + numbers[i + 1]
            elif operations[i] == 'm':
                result = result * numbers[i + 1]
            elif operations[i] == 's':
                result = result - numbers[i + 1]
        print(result)