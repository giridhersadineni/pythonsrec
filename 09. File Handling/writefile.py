filename=input("enter the name of the file")
f=open(filename,"w")
line=0
print("enter the content of the file")
while line<10:
    #f.write(input(line))
    #f.write("\n")
    print("Hello This is written using print Function",file=f)
    line=line+1

f.close()