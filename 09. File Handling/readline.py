filename=input("Enter the name of the file you want to read")
filereader=open(filename,"r")
ch=""
while ch != '\n':
    ch=filereader.read(1)
    print(ch,end="")
filereader.close