import datetime as dt
def time():
    days=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
    date=dt.datetime.now()
    print("Time:",date.time())
    print("Date:",date.date())
    print("Week Day ",days[date.weekday()])


time()