"""Prompt the user for a number either on a form input or the terminal. Depending on whether the number is even or odd,
display  either “odd” or “even” to the user."""

num = int(input("Enter your number: "))

if num % 2 == 0:
    print("Your number is: " + "Even")
else:
    print("Your number is: " +  "Odd")

#If the number is a multiple of 4, print out “divisible by 4”.
Your_num = int(input("Enter your number: "))

if num % 4 == 0:
    print("The number is divisible by 4")
else:
    print("The number is Not divisibe by 4")
