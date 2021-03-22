# a leap year is divisible by 4 and 400 and it should not be a millienial year 2000 2100

for year in range(2000,4001):
    if year % 4==0:
        if year % 100 == 0 and year % 400 !=0:
            continue
        elif year%400 ==0 :
            print(year)
        else:
            print(year)

