"""
Below program takes a positive integer and first checks if it's a four digit number.
If it is, it tells you the sum of the first and last digit.
Otherwise, it simply tells you it is not a four-digit number
"""
num = -1
while num < 0:
    num = int(input("Type in a number: "))
if num >= 1000 and num <= 9999:
    first_digit = num // 1000
    second_digit1 = num - (first_digit * 1000)
    second_digit2 = second_digit1 // 100
    second_digit3 = second_digit1 - (second_digit2 * 100)
    second_digit4 = second_digit3 // 10
    second_digit5 = second_digit3 - (second_digit4 * 10)
    combined_digit = first_digit + second_digit5
    print("The sum of the first and last digit of this number is:", combined_digit)
else:
    print("This is not a four-digit number")