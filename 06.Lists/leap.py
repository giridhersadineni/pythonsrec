leapyears=0
for year in range(2000,3000,4):
    if(year%100!=0):
        leapyears=leapyears+1
        print(year)
print((366*leapyears)+(365*(1000-leapyears)))
