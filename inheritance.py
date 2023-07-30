# example of inheritance
#defining parent class
class person():
     def value(self,name,age,asset):
         print(name)
         print(age)
         print(asset)
objpar=person()
objpar.value('keerthi',21,1000000000)

#creating child class
class child(person):
    def getip(self):
        global st,place,city
        st=input('street name')
        place=input('place name')
        city=input('city name')
    def disp(self):
        print(st)
        print(place)
        print(city)

#creating object for parent
parobj=person()
chiobj=child()
#calling parent method
parobj.value('tamil',21,10000000)
#calling child object
chiobj.getip()
chiobj.disp()
            
