import area_package

#Area of a circle
n1=int(input('Enter the radius of the circle:'))
print('Area of a circle',area_package.c(n1))


#Area of a square
n2=int(input('Enter the length of a side:'))
print('Area of a square',area_package.s(n2))

#Area of a rectangle
n3=int(input('Enter the length of the rectangle:'))
n4=int(input('Enter the width of the rectangle:'))
print('Area of a rectangle',area_package.r(n3,n4))

#Area of a triangle
n5=int(input('Enter the height of the triangle:'))
n6=int(input('Enter the base of the triangle:'))
print('Area of a triangle',area_package.t(n5,n6))
    
