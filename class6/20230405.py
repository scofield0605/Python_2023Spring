

class Person:
# Constructor
    def __init__(self, name, age, favoriteFood):
        self.name = name
        self.age = age
        self.favoriteFood = favoriteFood
    def introduce (self):
        print("我是"+ self.name +"，我今年"+ str(self.age)+"歲，最喜歡吃"+ self. favoriteFood +"。 ")
    def shout (self, content):
        print("我大喊：「"+ content+"」")
amy = Person( "Any", 15, "Apple")
amy.introduce ()
amy.shout("我討厭看牙醫！")


class Person:
    state = "healthy"
    def getCold( self):
        self.__class__.state='sick'
amy=Person ()
print("Origi"+ Person. state +".")
amy.getCold
print("After getCold(): I'm "+ Person.state +".")


#汽車類别
class Cars:
    door = 4 #類別屬性：屬於類別的屬性，而不是物件
# 實體方法(Instance Method)
    def drive(self):
        self._class_.door = 5
print ("Cars original door: ", Cars.door)
mazda = Cars ()
mazda.drive()
print ("Cars new door: ", Cars. door)





class Person:
#建構式
    def _init_(self, eyesColor, hairColor):
        self.eyesColor = eyesColor
        self. hairColor = hairColor
#美國人
    @classmethod
    def american (cls):
        return cls ("blue", "brown")
#台灣人
    @classmethod
    def taiwanese (cls):
        return cls ("black", "black") 
    def introduce (self):
        print("My eyes is {} and my hair is (}.".format (selseyescolor, self.haircolor))
amy = Person.american ()
ben = Person. taiwanese()
amy. introduce ()
ben.introduce ()



