print ('------------- Current date and time ----------------')
import time 
now = time.localtime(time.time())
print('Current date and time: ', time.strftime('%m/%d/%y , %H:%M:%S', now))
print('The current date: ' , time.strftime('%b %d, %y' , now))
print('day of the month: ', time.strftime('%d' , now))
print('The current time: ' , time.strftime(' %H:%M:%S' , now))

print ('------------- Month ----------------')
print('The current month as a number: ' , time.strftime('%m' , now))
print('The current month in full month name:' , time.strftime('%B' , now))
print('The current month in abbreviated month name:' , time.strftime('%b' , now))

print ('------------- Week ----------------')
t = time.localtime ()
print('Weekday in full weekday name: ' , time.strftime('%A' , now))
print('Weekday in abbreviated weekday name:' , time.strftime('%a' , now))
print('Weekday as a number: ' , t.tm_wday)

print ('------------- Relative to year ----------------')
from datetime import date

weekNumber = date.today().isocalendar()[1]
print('Week number of the year:' , weekNumber)
print('Day of the year as a number', t.tm_yday)
