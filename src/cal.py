"""
The Python standard library's 'calendar' module allows you to 
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `calendar.py month [year]`
and does the following:
 - If the user doesn't specify any input, your program should 
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
   
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
   
   
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that 
   month and year.
   
   
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.
"""

import sys
import calendar
from datetime import datetime

# print(len(sys.argv))
# print(sys.argv[0])
# if len(sys.argv == 1):
#     m = datetime.now().month
#     y = datetime.now().year
# print(calendar.month(y, m))

# elif len(sys.argv) == 2:
#     if len(sys.argv[1].isdigit) == 2:
#         m = int(sys.argv[1])
#     else:
#         format_err
#         exit()
#     y = datetime.now().year
# else:
#     if len(sys.argv[2]) == 6:
#         if sys.argv[1].isdigit() and sys.argv[2][1:5].isdigit():
#             m = int(sys.argv[1])
#             y = int(sys.argv[2][1:5])
#         else:
#             format_err
#             exit()
#     else:
#         format_err
#         exit()
# # I want to get the date now.
date = datetime.now()

# I want to get both the month, year from the user and split it.
datenow = input(
    "You must enter a month using 1-12 [space] and year (ie. 2017): ").split()

if len(datenow) == 0:
    print(calendar.month(date.year, date.month))
elif len(datenow) == 1 and datenow[0].isdigit() and (int(datenow[0]) <= 12):
    month = int(datenow[0])
    print(calendar.month(date.year, month))
elif len(datenow) == 2 and datenow[0].isdigit() and datenow[1].isdigit() \
        and (int(datenow[0]) <= 12) and (len(datenow[1]) == 4):
    month = int(datenow[0])
    year = int(datenow[1])
    print(calendar.month(year, month))
else:
    print(
        'You must enter a number between 1 and 12 for the first number. And then [space] and year format.'
    )

# number_of_days = int(input('Enter number of days in month: '))
# first_weekday = input('First weekday of the month: ')

# weekdays = {'Su': 0, 'M': 1, 'T': 2, 'W': 3, 'Th': 4, 'F': 5, 'Sa': 6}
# print('{:>3}{:>4}{:>4}{:>4}{:>4}{:>4}{:>4}'
#       .format('Su', 'M', 'T', 'W', 'Th', 'F', 'Sa'))

# print (weekdays[first_weekday]*4*' ' + '{:>3}'.format(1), end=' ')
# for current_day in range(1, number_of_days+1):
#     # Second elif block
#     if (weekdays[first_weekday] + current_day) % 7 == 0:
#         print ()
#     print ('{:>3}'.format(current_day ), end=' ')