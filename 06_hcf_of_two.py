# find HCF/GCD of two numbers
# Method 1: iterative method

a, b = 16, 80

hcf = 1

lower = min(a, b)
for i in range(1, lower + 1):
    if (a % i == 0) and (b % i == 0):
        hcf = i # this will keep assigning/overwrite value of i to hcf until the last iteration and thus we will have the max/highest division common factor
print(hcf)

# method 2: recursive method

def hcf(a, b):
    # Logic: Keep dividing numbers and taking remainder
    # Until remainder becomes zero, the last non-zero number is HCF
    # 1. If second number becomes zero, first number is HCF
    # 2. Swap numbers and take remainder in each recursive call
    # 3. Keeps reducing numbers until remainder is zero
    if b == 0:
        return a
    return hcf(b, a % b)
