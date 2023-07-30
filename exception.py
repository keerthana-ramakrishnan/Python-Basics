#exceptions
#exception handling
i=[10,20,30,40,50,60]
a=int(input('type value for a'))
b=int(input('type value for b'))
try:
    print(i[6])
except IndexError:
    print('index error happened')

try:
    print(a/c)
except NameError:
    print('nameerror happened')

try:
    print(a/b)
except ZeroDivisionError:
    print('division by zero error happened, change denominator with non zero values')
print('hai')

try:#when we don't know what exception may occur then we can just a default except
    print(i/j)
except:
    print('exception hapned')

try:#A try block can have any number of except blocks
    print(i[6])
    print(a/c)
    print(a/b)
except IndexError:
    print('index error happened')
except NameError:
    print('nameerror happened')
except ZeroDivisionError:
    print('division by zero error happened, change denominator with non zero values')

#Exception example with else block
try:
    k=(a+b)/(a-b)
except ZeroDivisionError:
    print('division by zero error happened')
else:
    print('No exception happened')

#Exception example with Finally block
try:
    k=(a+b)/(a-b)
except ZeroDivisionError:
    print('division by zero error happened')
else:
    print('No exception happened')
finally:#this will get executed when there is any exception or not
    print('execution over')
