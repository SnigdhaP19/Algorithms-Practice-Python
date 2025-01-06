"""
Below takes in a number and first checks if it's a five digit number or not.
If it is, it will give you the middle digit
If it is not, it will tell you it is not a five-digit number.
Please note for this program, negative numbers are not applicable
"""
num = -1
while num < 0:
    num = int(input("Type in a number: "))
if num >= 10000 and num <= 99000:
    div_num1 = num % 1000
    div_num2 = div_num1 // 100
    print("The middle number of this number is:", div_num2)
else:
    print("This is not a five-digit number")