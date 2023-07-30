class area():#Class Creation- class classname():
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
a=int(input('\nenter the lenght of a side:'))
ar=area()#Object Creation- Object_name=Class_name
ar.sq(a)#Method Calling-  Object_name.Method_name(argument)

r1=int(input('\nEnter the length of the rectangle:'))
r2=int(input('Enter the width of the rectangle:'))
ar.rect(r1,r2)

c=int(input('\nEnter the radius of the circle:'))
print('area of circle:',ar.circle(c))

t1=int(input('\nEnter the height of the triangle:'))
t2=int(input('Enter the base of the triangle:'))
print('area of triangle:',ar.triangle(t1,t2))


'''
class Area:
    def __init__(self, a):
        self.a = a

    def sq(self):
        area_sq = self.a * self.a
        print('Area of square:', area_sq)

a = int(input('Enter the length of a side: '))
ar_obj = Area(a)
ar_obj.sq()
'''
