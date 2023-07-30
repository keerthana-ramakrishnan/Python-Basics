#Arihmetic, Logical and Bitwise operations using lambda function

#Arithmetic Operators
a=lambda a,b:a+b
b=lambda a,b:a-b
c=lambda a,b:a*b
d=lambda a,b:a/b
e=lambda a,b:a//b
f=lambda a,b:a%b

n1=int(input('Enter a number:'))
n2=int(input('Enter a another number:'))
n3=int(input('Enter a another number:'))
print('\nAddition:',a(n1,n2))
print('Subtraction:',b(n1,n2))
print('Multiplication:',c(n1,n2))
print('Division:',d(n1,n2))
print('Double Slash:',e(n1,n2))
print('Modulus:',f(n1,n2))

#Logical Operators
g=lambda a,b,c:a<b and b<c and a==b
print('\nAND:',g(n1,n2,n3))
h=lambda a,b,c:a<b or b<c
print('OR:',h(n1,n2,n3))
i=lambda a,b,c: not b<c
print('NOT:',i(n1,n2,n3))

#Bitwise Operators
j=lambda a,b:a & b
print('\nbitwise AND',j(n1,n2))
k=lambda a,b:a | b
print('\nbitwise OR',k(n1,n2))
l=lambda b:~b
print('\nbitwise Complement',l(n2))
m=lambda a,b:a ^ b
print('\nbitwise Ex-OR',m(n1,n2))
n=lambda b:b<<2
print('\nbitwise Left Shift',n(n2))
o=lambda b:b>>2
print('\nbitwise Right Shift',o(n1))



