#using function
'''class addition():
    a=10
    b=18
    def addi(a,b):
        c=a+b
        return c
    d=int(input('enter'))
    e=int(input('enter'))
    print(addi(d,e))


#calculate the area of square
class area():
    a=int(input('enter the lenght of a side:'))
    s=a*a
    print(s)
obj1 = area() '''   


#using object
class area():
    a=int(input('enter the lenght of a side:'))
    def sq(self):
        area_sq=a*a
        print('area of square',area_sq)
ar_obj=area()
ar_obj.sq()
ar_obj.rect()
