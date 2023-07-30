'''
4. Write a python script to sum the series up to the given numbers
I add the N numbers
Ii add the ODD numbers
Iii Add the even numbers '''
n=int(input("Enter a number:"))
a=(n*(n+1))/2
print('Sum of serier up to the given number is',a)
a=0
for i in range(1,n+1,2):
    print(i)
    a+=i
print('Sum of serier of odd numbers up to the given number is',a)
a=0
for i in range(0,n+1,2):
    a+=i
print('Sum of serier of even numbers up to the given number is',a)
