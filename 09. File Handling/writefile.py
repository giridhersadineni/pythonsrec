filename=input("enter the name of the file")
filewriter=open(filename,"w")
mydata='''
This is a 
sample text 
written from
variable
'''
content=( input ( " enter the content of the file " ) )
filewriter.write(content)
filewriter.write("\n")
filewriter.write(mydata)
filewriter.close()