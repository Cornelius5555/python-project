"""TASK 9: Using Python or PHP or Java or Ruby or JavaScript
Write a program called stars. It should prompt the user for a number, and it should print the number of stars till the number entered.
Example If rows is 5, it should print the following:
*
**
***
****
*****....."""
"""my_num = ""
output = ""
for i in my_num:
    my_num = 5
    your_num = input("Enter your number: ")
    if your_num == my_num:
        print("hurray")
        break
    else:
        output = "*"
        i += 1
        print(output)"""
stars = ""
number = int(input("Enter your number: "))
for i in range(number):
    stars += '*'
    print(stars)
