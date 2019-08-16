name=input("enter your name")
fathername=input("enter your father name")
print("enter six subject marks")
marks=[]
sum=0
for i in range(6):
    marks.insert(i,int(input("Enter Marks:")))
    sum=sum+marks[i]
print("Total:",sum)
print("Average",sum/6)
marks.sort()
print("You got maximum marks of",marks[len(marks)-1])
print("You scored Lowest of",marks[0])
