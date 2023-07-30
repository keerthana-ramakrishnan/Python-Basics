'''2. Create a class with 5 methods for calculating the areas of shapes such as square,
rectangle,triangle, circle and rohmbus. Make sure that the class have these methods with
different types.
    i)Create an object which will find the area of square and rectangle
    ii)Create an another object to find out the areas of triangle and circle. 
    iii. Make one more instance to calculatethe areas of rohmbus and triangle
    iv. Have 4th instance for calculating the areas of all shapes.'''

class area():
    def sq(self,a):
        s=a*a
        print('area of square',s)
    def rect(self,l,w):
        r=l*w
        print('area of rectangle',r)
        return r
    def circle(self,r):
        c=3.14*r**2
        return c
    def triangle(self,h,b):
        t=(h*b)/2
        return t
    def rhombus(self,p,q):
        rh=0.5*p*q
        return rh

ar=area()

#Area of Square and Rectangle
a=int(input('\nenter the lenght of a side:'))
ar.sq(a)

r1=int(input('\nEnter the length of the rectangle:'))
r2=int(input('Enter the width of the rectangle:'))
ar.rect(r1,r2)

#Area of Circle and Triangle
c=int(input('\nEnter the radius of the circle:'))
print('area of circle:',ar.circle(c))

t1=int(input('\nEnter the height of the triangle:'))
t2=int(input('Enter the base of the triangle:'))
print('area of triangle:',ar.triangle(t1,t2))

#Area of Rhombus
rh1=int(input('\nEnter the value of diagonal 1:'))
rh2=int(input('Enter the value of diagonal 2:'))
print('area of rhombus:',ar.rhombus(rh1,rh2))
