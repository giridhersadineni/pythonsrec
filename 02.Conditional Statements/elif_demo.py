a=int(input("Enter a Number"))
b=int(input("Enter another Number"))
c=int(input("One more Please!!"))
d=int(input("One more ! last One !!!! "))
if a>b and a>c and a>d:
    print(a)
elif b>c and b>d:
    print(b)
elif c>d:
    print(c)
else:
    print(d)