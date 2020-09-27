Sample Input:
08 05 2015

Sample Output:
WEDNESDAY
-----------------------------------------------------------------

import calendar

month,day,year=map(int,input().split())
print((calendar.day_name[calendar.weekday(year,month,day)]).upper())
