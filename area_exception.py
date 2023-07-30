#To calculate the area of triangle and implement at least 3 exceptions(use else and finally clause)

t1=int(input('Enter the height value of the triangle:'))
t2=int(input('Enter the base value of the triangle:'))
try:
    t=(t1*t2)/2
except NameError:
    print('nameerror happened')
except ZeroDivisionError:
    print('division by zero error happened')
except TypeError:
    print('typeerror happened')
else:
    print(t)
finally:
    print('Area of triangle calculated')
