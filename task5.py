"""TASK 5: Using Python or PHP or Java or Ruby or JavaScript
Implement a program that takes 3 form inputs or from the terminal, and stores them in three variables. Return the largest of the three. Do this without using the the inbuilt max () function!
The goal of this exercise is to think about some internals that programs normally take care of for us. """
num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))
num3 = int(input("Enter 3rd number: "))
if num1 > num2 and num1 > num3:
    print(f"1st number is the largest: {num1}")
elif num2 > num1 and num2 > num3:
    print(f"2nd number is the largest: {num2}")
else:
    print(f"3rd number is the largest: {num3}")