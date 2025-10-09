import datetime 
current_date=datetime.datetime.now()
new_date=current_date - datetime.timedelta(days=5)
print("Current Date:", current_date)
print("Date 5 days ago:", new_date)