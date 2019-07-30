a=int(input("Enter a Number"))
b=int(input("Enter another Number"))
c=int(input("One more Please!!"))
d=int(input("One more ! last One !!!! "))
if a>b:
    if a>c:
        if a>d:
            print(a)
        else:
            print(d)
    else:
        if c>d:
            print(c)
        else:
            print(d)
else:
    if b>c:
        if b>d:
            print(b)
        else:
            print(d)
    else:
        if c>d:
            print(c)
        else:
            print(d)
    