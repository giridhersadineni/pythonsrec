studentrows=['roll','name','tel','hin','eng','total']
studentrecord=dict.fromkeys(studentrows)
allstudmarks={}
print("How many students result do you need to calculate")
totalstudents=int(input())
for i in range(totalstudents):
    print("Enter Details of student's Result")
    record=studentrecord.copy()
    record['roll']=int(input("Enter the Roll Number:"))
    record['name']=input("Enter the Name of The Student:")
    record['tel']=int(input("Marks of Telugu:"))
    record['hin']=int(input("Marks of Hindi:"))
    record['eng']=int(input("Marks of English:"))
    record['total']=record['tel']+record['hin']+record['eng']
    allstudmarks[record['roll']]=record


for result in allstudmarks.values():
    # print(result)
    print(result['roll'],result['name'],result['tel'],result['hin'],result['eng'],result['total'])

