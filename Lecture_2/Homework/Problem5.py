import time
import datetime
import calendar

bday = datetime.date(2019, 9, 30)
tday = datetime.date.today()

localtime = datetime.datetime.now()

till_bday = bday - tday


print ("My birthday is: " ,bday)
print('Year: ', bday.year)
print('Month: ', bday.month)
print('Day: ', bday.day)
print('Day of the week (version 1): ', bday.isoweekday())
print('Day of the week (version 0): ', bday.weekday())
print("Days until my next birthday: ", till_bday)

 
print ("The calendar:")
print (calendar.month(2017, 5))
 
one_day = datetime.timedelta(days = 1)

print('Yesterday : ',localtime -one_day, "\nafter 3 days", localtime + 2* one_day, "\n befire 3 days: ", localtime -4*one_day )