
import datetime
import pytz

dt=datetime.datetime(2018,7,26,9,30,45,100000,tzinfo=pytz.UTC)
#print(dt)


dt_utcnow=datetime.datetime.now().replace(tzinfo=pytz.UTC)
#print(dt_utcnow)



dt_utcnow=datetime.datetime.now(tz=pytz.UTC)
#print(dt_utcnow)
# for tz in pytz.all_timezones:
#     print(tz)

dt_ktm=dt_utcnow.astimezone(pytz.timezone('Asia/Kathmandu'))

print(dt_ktm)


#Implement to naive datetime
sys_dt=datetime.datetime.now()
dt_ldn=pytz.timezone('Europe/London')

dt_ktm=sys_dt.astimezone(pytz.timezone('Asia/Kathmandu'))
print(dt_ktm)



###################
dt_ktm=datetime.datetime.now(tz=pytz.timezone('Asia/Kathmandu'))
print(dt.strftime('%B %d, %Y'))

##Str to datetime
dt_str='July 20, 2018'
dt=datetime.datetime.strptime(dt_str,'%B %d, %Y')
print(dt)


