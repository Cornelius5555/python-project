"""TASK 7: Using Python or PHP or Java or Ruby or JavaScript
Write that prompts the user to input student marks. The input should be between 0 and 100.Then output the correct grade: 
A > 79 , B - 60 to 79, C -  59 to 49, D - 40 to 49, E - less 40"""
marks = range(0, 101)
grade =int(input("Enter your Grade: "))
if grade in marks:
    if grade > 79:
      print("A")
    elif grade > 60 and grade < 79:
      print("B")
    elif grade > 59 and grade < 49:
      print("C")
    elif grade > 49 and grade < 40:
      print("D")
    else:
      print("E")
else:
  print("Invalid grade entered")
    