"""TASK 4: Using Python or PHP or Java or Ruby or JavaScript
Write a program which accepts email as form input or from terminal. Validate the email by checking if it's a valid email. 
Hint: Check if it contains an “@” symbol and “.” symbol."""
email = input("Enter your email: ")
if "@" in email and "." in email:
    print("valid email")
else:
    print("Invalid email")