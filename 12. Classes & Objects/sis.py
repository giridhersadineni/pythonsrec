class student:
    '''
    This represents student data
    '''
    name=""
    fathername=""
    rollno=0
    marks=[]
    __total=0
    average=0

    def __init__(self,rollno,name):
        self.rollno=rollno
        self.name=name
        self.get_details()


    def calculate(self):
       for i in self.marks:
           self.total=self.total+i
       self.average=self.total/len(self.marks)

    def get_details(self):
        self.fathername=input("Enter Father Name")
        for i in range(3):
            self.marks.append(int(input("Enter Marks")))
   
    def display(self):
        '''
        Displays Student Data
        '''
        print("Roll No",self.rollno)
        print("Name:",self.name,"Father Name:",self.fathername)
        print("Marks: ",self.marks)
        print("Total",self.total)

    
    def storetodb():
        pass

while  True:
    print("Enter Choice","1.Add a Student","2.Display Details",sep="\n")
    choice=int(input("Enter Operation Number"))
    if choice==1:
        roll=int(input("Enter rollnumber"))
        name=input("Enter the name of the student")
        s=student(roll,name)
    elif choice==2:
        s.display()
    elif choice==3:
        s.storetodb()

    else:
        print("Invalid Choice")