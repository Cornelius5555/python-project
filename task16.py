"""TASK 16: Using Python or PHP or Java or Ruby or JavaScript
Continue with the program above, then use  the gross salary to find the NSSF. 
To find the Kenya NSSF Rate using. Compute NSSF using 6% of the Gross Salary. BUT ONLY A MAXIMUM OF 18,000 CAN BE USED IN NSSF. """

basic_salary = int(input("Enter basic aslary: "))
benefits = int(input("Enter benefits: "))
gros_salary = basic_salary + benefits
print(gros_salary)

#nhif
nhif = ""
if gros_salary < 6000:
     nhif = 150
elif gros_salary > 6000 and gros_salary < 7999:
      nhif = 300
elif gros_salary > 7999 and gros_salary < 11999:
      nhif = 400
elif gros_salary > 11999 and gros_salary < 14999:
      nhif = 500
elif gros_salary > 14999 and gros_salary < 19999:
      nhif = 600
elif gros_salary > 19999 and gros_salary < 24999:
      nhif = 750
elif gros_salary > 24999 and gros_salary < 29999:
      nhif = 850
elif gros_salary > 29999 and gros_salary < 34999:
      nhif = 900
elif gros_salary > 34999 and gros_salary < 39999:
      nhif = 950
elif gros_salary > 39999 and gros_salary < 44999:
      nhif = 1000
elif gros_salary > 44999 and gros_salary < 49999:
      nhif = 1100
elif gros_salary > 49999 and gros_salary < 59999:
      nhif = 1200
elif gros_salary > 59999 and gros_salary < 69999:
      nhif = 1300
elif gros_salary > 69999 and gros_salary < 79999:
      nhif = 1400
elif gros_salary > 79999 and gros_salary < 89999:
      nhif = 1500
elif gros_salary > 89999 and gros_salary < 99999:
      nhif = 1600
else:
      nhif = 1700
print(nhif)

nssf = ""
if gros_salary > 0 and gros_salary <= 18000:
      nssf = gros_salary * 0.06
else:
      nssf = 18000 * 0.06
print(nssf)