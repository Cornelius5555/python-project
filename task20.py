"""Task 20: Using Python or PHP or Java or Ruby or JavaScript
Continue with the same program and calculate an individual’s Net Salary using:
 net_salary = gross_salary - (nhif + nhdf +  nssf + payee)"""


basic_salary = int(input("Enter basic salary: "))
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

#nhdf
nhdf = gros_salary * 0.015
print(nhdf)

#taxable income
taxable_income = gros_salary - (nssf + nhdf)
print(taxable_income)


payee = ""
if taxable_income <= 24000:
      payee = 2400
elif taxable_income > 24000 and taxable_income < 32333:
      payee = ((taxable_income - 24000) * 0.25) + (24000 * 0.1) - 2400
elif taxable_income > 32333 and taxable_income < 500000:
      payee = ((taxable_income - 32333) * 0.3) + (24000 * 0.1) + (8333 * 0.25)- 2400
elif taxable_income > 50000 and taxable_income < 800000:
      payee = ((taxable_income - 500000) * 0.325) + (24000 * 0.1) + (8333 * 0.25) + (467667 *0.3) - 2400
else:
      payee = ((taxable_income - 800000) * 0.35) + (24000 * 0.1) + (8333 * 0.25) + (467667 * 0.3) + (300000 * 0.325) - 2400
print(payee)

net_salary = gros_salary - (nhif + nhdf +  nssf + payee)
print(net_salary)