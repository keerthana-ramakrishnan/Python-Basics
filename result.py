n=str(input('enter your name:'))
c=int(input('enter your class'))
t=int(input('enter your tamil mark:'))
e=int(input('enter your english mark:'))
m=int(input('enter your maths mark:'))
s=int(input('enter your science mark:'))
p=int(input('enter your physics mark:'))
r=t+e+m+s+p
avg=r/5
if(t&e&m&s&p)>40):
    if(avg>80):
        g='O'
    elif(avg>60):
        g='A'
    elif(avg>50):
        g='B'
    else:
        g='C'
else:
    g='Fail'
l='-------------------------------------------------------------------------'
print(l)
print('|\t\tSri Ranganathar institute of engineering and technology\n|')
print('|\t\t\t\t\tResults\n|')
print('|name of the student:',n,)
print('|class',c,)
print('|\n|Marks',)
print('|\tTamil:',t)
print('|\tEnglish:',e)
print('|\tMaths:',m)
print('|\tScience:',s)
print('|\tPhysics:',p)
print('|\n|\t\tResult:',r)
print('|\n|\tGrade of the Student:',g)
if(g=='|Fail'):
    print('|\n|\tBetter Luck Next Time')
else:
    print('|\n|\tCongragulations!')
print(l)
