# find lcm of two numbers
#iterative method

a, b = 32, 40

hcf = 1

lower = min(a, b)

for i in range(1, lower + 1):
    if (a % i == 0) and (b % i == 0):
        hcf = i
result_hcf = hcf

# lcm formula = lcm(a, b) * hcf(a, b) = a * b

lcm = int((a * b) / result_hcf)
print("lcm: ", lcm)