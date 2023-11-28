"""TASK 6:Using Python or PHP or Java or Ruby or JavaScript
Write a program input a password. Give them only 4 attempts to check the passwords entered against “admin@123”. 
If the password is correct access is granted. After you show them a message , the account is blocked."""
password = "admin@123"
attempts = 4
for i in range(attempts):
    your_pass = input("Enter your pass: ")
    if your_pass == password:
        print("Access granted")
        break
    else:
        attempts += 1
        if attempts < 4:
            print("Wrong pass")
            attempts-i-1
        else:
            print("Account locked")