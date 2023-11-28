"""TASK 11: Using Python or PHP or Java or Ruby or JavaScript
Write a program that takes the date of birth of a person and the program outputs the age in terms of years,months,days TODAY."""
import datetime


date_ofbirth = input("Enter date: ")
month = input("Enter month: ")
year = input("Enter Year: ")
birthday = datetime(year, month, date_ofbirth)
print(birthday)