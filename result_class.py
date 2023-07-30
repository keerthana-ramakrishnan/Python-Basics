class result():
    
    def Result(self,t,e,m,s,p):
        re=t+e+m+s+p
        return re
    def grade(self):
        avg=(t,e,m,s,p)/5
        if((t&e&m&s&p)>40):
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
        return g
re=result()

n=str(input('enter your name:'))
c=int(input('enter your class'))
t=int(input('enter your tamil mark:'))
e=int(input('enter your english mark:'))
m=int(input('enter your maths mark:'))
s=int(input('enter your science mark:'))
p=int(input('enter your physics mark:'))

re.Result(t,e,m,s,p)
re.grade()

        
