'''1. Write a python script to implement the module datatime and check all the 
functions of strftime().
1. Assume that the date time is 13th February 2011
2. Consider the current date for performing all the functions of strftime()
3. Check these functions with the object 27th October 2019
i)Find out the date , month and day separately
ii) shorter version of the day ,month and year of all the above dates
iii) print the month as number
iv) print the week as number
v)print the hour both in 24 hrs and 12 hr format
vi) print the ,micro seconds, seconds and minutes of the time
vii) print the day number of the year'''

from datetime import datetime

def dateTime(a):
    print("Date:", a.strftime('%d'))
    print("Month:", a.strftime('%B'))
    print("Day:", a.strftime('%A'))
    print("Shorter version of the day:", a.strftime('%a'))
    print("Shorter version of the month:", a.strftime('%b'))
    print("Shorter version of the year:", a.strftime('%y'))
    print("Month as number:", a.strftime('%m'))
    print("Week as number:", a.strftime('%U'))
    print("Hour (24-hr format):", a.strftime('%H'))
    print("Hour (12-hr format):", a.strftime('%I'))
    print("Microseconds:", a.strftime('%f'))
    print("Seconds:", a.strftime('%S'))
    print("Minutes:", a.strftime('%M'))
    print("Day number of the year:", a.strftime('%j'))
    
date = input("Enter a date (dd/mm/yyyy): ")
date = datetime.strptime(date, '%d/%m/%Y')
print("Date components for the given date:")
dateTime(date)

#usage:
#strftime()- extract specific date and time
# %d, %B, and %A - extract the date, full month name, and full day name
#%a, %b, and %y -  abbreviated day name, abbreviated month name, and the last two digits of the year
# %m and %U - extracts the month as a two-digit number and  week number
#%H and %I- extracts hour in 24-hour format and  hour in 12-hour format.
# %f, %S, and %M - extract microseconds, seconds, and minutes
#%j - extracts the day number of the year.
