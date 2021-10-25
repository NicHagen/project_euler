""" 
You are given the following information, but you may prefer to do some research 
for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.

A leap year occurs on any year evenly divisible by 4, but not on a century 
unless it is divisible by 400.
How many Sundays fell on the first of the month during the twentieth century 
(1 Jan 1901 to 31 Dec 2000)?
"""

from datetime import date

count = 0
# get the ordinal (number of days from year 1 January 1) of the start and end
# dates to create loop
for i in range(date(1901,1,1).toordinal(), date(2000,12,31).toordinal()+1):
    # if the ordinal is the first of the month and is a sunday, add 1 to count
    if date.fromordinal(i).day == 1 and date.fromordinal(i).weekday() == 6:
        count += 1

print(count)
