"""TASK 4: Using Python or PHP or Java or Ruby or JavaScript
Write a program which accepts email as form input or from terminal. Validate the email by checking if it's a valid email. 
Hint: Check if it contains an “@” symbol and “.” symbol."""

output = ""
email = input("Enter email: ")
if "@" in email and "." in email:
    if email.index("@") < email.index("."):
        output = "Valid email"
    else:
        output = "Invalid email, (@) should come before (.)"
else:
    output = "Invalid email"

print(output)