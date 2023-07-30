'''def asm(*kids):
    n=0
    for n in range(0,len(kids)-1):
        print(kids[n])
print(asm('divya', 'iiibe',89))'''


#using iterator

def name(n,c,*marks):
    print(n)
    print(c)
    for i in marks:
        print(i)
name('divya','iiibe',89,65,98,99)
