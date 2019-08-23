filename=input("Enter the name of the file you want to read")
fr=open(filename,"r")
ch=""

# def readline(FileReader):   
#     line=""
#     ch=""
#     while ch != '\n':
#         ch=FileReader.read(1)
#         line=line+ch
#     return line
# for i in range(10):
#     print(readline(fr),end="")

for line in fr:
    print(line)