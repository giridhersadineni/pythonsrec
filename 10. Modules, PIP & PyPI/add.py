import sys
sum=0
if(len(sys.argv)<3):
    print("Need minimum 2 numbers to add")
    exit()
numbers=sys.argv[1:len(sys.argv)]
for i in numbers:
    sum=sum+int(i)
print(sum)