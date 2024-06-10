import datetime

from pytz import timezone

## with timezone
def getDateOnly():
    now = datetime.datetime.now(timezone('Asia/Kolkata'))     # datetime with a particular timezone
    datetimeee=datetime.datetime(
            now.year, now.month, now.day,now.hour,now.minute,now.second)    # 
    datetimee=str(datetimeee)         
    return datetimee


## without timezone
def getDateOnly():
    now = datetime.datetime.now()     # datetime based on system's timezone
    datetimeee=datetime.datetime(
            now.year, now.month, now.day,now.hour,now.minute,now.second)    # 
    datetimee=str(datetimeee)         
    return datetimee