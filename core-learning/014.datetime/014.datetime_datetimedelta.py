
import datetime

dt=datetime.datetime(2018,7,26,9,30,45,100000)
print(dt)
print(dt.date())
print(dt.time())
print(dt.year)


tdelta=datetime.timedelta(days=7,hours=7)
print(dt+tdelta)


dt_today=datetime.datetime.today()
dt_now=datetime.datetime.now() #Allows us to set timezone
dt_utcnow=datetime.datetime.utcnow()

print(dt_today)
print(dt_now)
print(dt_utcnow)


