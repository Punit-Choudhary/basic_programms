#!pytho3
#birthday_million_pi.py - checks wheather your birthday appears in first million digit of pi value.

with open('one_million_pi.txt') as file:
  lines = file.readlines()

pi_string = ''
for line in lines:
  pi_string += line.rstrip()

birthday = input("Enter your birthday (format: mmddyy) : ")
if birthday in pi_string:
  print("Your birthday appears in first million digits of pi value!")
else:
  print("Your birthday does not appear in first million digits of pi value.")
