import datetime

gigasecond = datetime.timedelta(seconds=1000000000)
date = datetime.datetime(datetime.date.today().year, datetime.date.today().month, datetime.date.today().day)+gigasecond
print(date)