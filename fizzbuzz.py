"""The code below takes in a number and prints FizzBuzz if it's a multiple of 3 and 5.
If it's a multiple of only 3, it will print Fizz. If it's a multiple of 5, it will only print 5.
Otherwise, it will print Hello World. 
"""
num = int(input("Enter a number: "))
if (num % 3 == 0) and (num % 5 == 0):
    print("FizzBuzz")
elif num % 3 == 0:
    print("Fizz")
elif num % 5 == 0:
    print("Buzz")
else:
    print("Hello World")