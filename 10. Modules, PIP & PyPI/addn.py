import sys
def add(a,b,*argtuple):
    '''
    def add(a,b,**argtuple):
    This function returns the sum of any number of values passed to it
    Arguments: 
    a,b Mandatory
    '''
    sum=a+b
    for i in argtuple:
        sum=sum+i
    return sum

n=int(input("Enter how many numbers you want to add"))
if(n<2):
    print("I need minimum two numbers to add")
    exit(1)
l=[]
for i in range(n):
    l.append(int(input("enter number")))
print(add(l[0],l[1],*l[2:len(l)]))
