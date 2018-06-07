from datetime import date, datetime


date1 = date.today().strftime('%m/%d/%Y')
date2 = 12/22/2014
diff = str(datetime.strptime(date1, '%m/%d/%Y')-datetime.strptime(date2, '%m/%d/%Y')).split()[0]

print(diff)