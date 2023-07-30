#no parameter no return
def addi():
    a=int(input( 'enter the value of a:'))
    b=int(input( 'enter the value of b:'))
    c=a+b
    print('addition of a and b is ',c)
    
print(addi())

#no parameter return
def addi():
    a=int(input( 'enter the value of a:'))
    b=int(input( 'enter the value of b:'))
    c=a+b
    print('addition of a and b is ',c)
    return c

print(addi())

#parameter no return
def addi(a,b):
    c=a+b
    print('addition of a and b is ',c)

m=int(input( 'enter the value of a:'))
n=int(input( 'enter the value of b:'))
print(addi(m,n))

#parameter return
def addi(a,b):
    c=m+n#it can be a,b or passed parameter
    print('addition of a and b is ',c)
    return c

m=int(input( 'enter the value of a:'))
n=int(input( 'enter the value of b:'))
print(addi(m,n))


