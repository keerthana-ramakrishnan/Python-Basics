'''Write a python program to read the name, age and marks for 5 subjects for 10 students using
arbitary arguments. And print the same using the arbitary elements'''

def stud(name, age, *marks):
    print('\t\t\tStudent details')
    print('Name of the Student',name)
    print('Age of the Student',age)
    a=-1
    for i in marks:
        sub=['TAMIL:', 'ENGLISH', 'MATHS', 'SCIENCE','SOCIAL SCIENCE']
        a+=1
        b=sub[a]
        print(b,i)
def getval():
        print('\t\t\tEnter Student Details')
        st_name=str(input('Enter the name of student:'))
        st_age=int(input('Enter the age of student:'))
        print('Enter student marks:')
        t=int(input('TAMIL:'))
        e=int(input('ENGLISH:'))
        m=int(input('MATHS:'))
        s=int(input('SCIENCE:'))
        ss=int(input('SOCIAL SCIENCE:'))
        return st_name, st_age, t,e,m,s,ss

for i in range(0,10):
    stud_data=getval()
    stud(*stud_data)
