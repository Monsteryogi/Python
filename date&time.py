#date and time in various format
from datetime import datetime                  #importing module datetime

print("dd/mm/yyyy and hh/mm/ss")
now= datetime.now()
print ( "Date: " + '%s/%s/%s' %(now.day,now.month,now.year))
print ( "Time: " + '%s:%s:%s'  %(now.hour,now.minute,now.second))

print("\nyyyy-dd-mm and hh/mm/ss")
print ( "Date: " + '%s-%s-%s' %(now.year,now.day,now.month))
print ( "Time: " + '%s:%s:%s'  %(now.hour,now.minute,now.second))



