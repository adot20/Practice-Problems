# check if a number is armstrong or not

number = input("enter your number: ")
digit_result = 0

# check armstrong:
for i in str(number):
    digit_result += int(i) ** 3
    

if int(number) == digit_result:
    print("Yes")
else:
    print("No")