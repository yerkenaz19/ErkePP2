import datetime
current_date=datetime.datetime.now()
yesterday=current_date - datetime.timedelta(days=1)
tomorrow=current_date + datetime.timedelta(days=1)
print(yesterday)
print(current_date)
print(tomorrow)