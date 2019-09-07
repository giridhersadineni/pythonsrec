students={}

def get_details():
    student=[]
    marks=[]
    roll=int(input("Enter student roll number"))
    name=input("Enter student name")
    student.append(name)
    fathername=input("Enter student father name")
    student.append(fathername)
    for i in range(6):
        marks.append(int(input("Enter subject marks")))
    student.append(marks)
    students[roll]=student
    
    
def display_result():
    roll=int(input("Enter the student number"))
    student=students.get(roll,-1)
    if(student==-1):
        print("Student Doesnt Exist")
        return
    total=0
    print("Name ",student[0],"\n","Father Name",student[1])
    print("Marks:",student[roll])
    for i in student[2]]:
        total=total+i
    print("Total Marks",total)
    print("Average ",total/6)

ch=0
switcher={1:get_details,2:display_result}
while 1:
    print("Enter 1 to add student",
    "enter 2 to view student details")
    ch=int(input())
    action=switcher.get(ch,-1)
    if(action==-1):
        print("Invalid Action")
    else:
        action()