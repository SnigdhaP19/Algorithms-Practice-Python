"""
Below takes in a positive integer and first checks if it's a three-digit number or not.
If it is, it adds up the first and last digit and tells if you the sum is even or odd
Otherwise, it simply tells you it is not a three-digit number
"""
num = -1
while num < 0:
    num = int(input("Type in a number: "))
if num >= 100 and num <= 999:
    first_digit = num // 100
    second_digit1 = num - (first_digit * 100)
    second_digit2 = second_digit1 // 10
    second_digit3 = second_digit1 - (second_digit2 * 10)
    combined_digit = first_digit + second_digit3
    if combined_digit % 2 == 0:
        print("The sum of the first digit and last digit is even.")
    else:
        print("The sum of the first digit and last digit is odd.")
else:
    print("This is not a three-digit number")