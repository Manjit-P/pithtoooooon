class dog:
    def eat(self):
        print('eating dog food')
class cat:
    def eat(self):
        print('eating cat food')
ani = dog()
mal = cat ()
ani.eat()
mal.eat()
class dog:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def __gt__(self,other):
        return True if self.age > other.age else False
tofer = dog('shes', 8)
syd =  dog('syd', 9)
print(tofer>syd)