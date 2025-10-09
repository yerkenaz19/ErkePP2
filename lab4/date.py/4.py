import datetime 
date_format="%Y-%m-%d %H:%M:%S"
date1_str=input("First date (YYYY-MM-DD HH:MM:SS): ")
date2_str=input("Second date (YYYY-MM-DD HH:MM:SS): ")
date1=datetime.datetime.strptime(date1_str,date_format)
date2=datetime.datetime.strptime(date2_str, date_format)
difference = abs(date2-date1)
print("Difference in seconds:", int(difference.total_seconds()))