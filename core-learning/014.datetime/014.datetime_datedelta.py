
import datetime

#timedelta=date1+date2
#date1=timedelta+date2

today=datetime.date.today()
tdelta=datetime.timedelta(days=7)
print(today+tdelta) #Afer 7 days date
print(today-tdelta) #Before 7 days date


afoolday=datetime.date(2019,1,1)
till_foolday=afoolday-today
print(till_foolday.days)#Find the days for next april fool day




t=datetime.time