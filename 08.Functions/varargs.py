#variable length arguments

def add(a,b,*argtuple):
    sum=a+b
    for val in argtuple:
        sum=sum+val
    return sum

print(add(1,2,3,2,3,5,4,5)

        