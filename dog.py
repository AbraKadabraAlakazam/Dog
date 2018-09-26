class Dog:
    name = "Woofers"
    color = "black"

    def Bark(self):
        print("Woof my name is " + self.name + "!")


mydog = Dog()
mydog.name = "Glock"
print(mydog.name + " is " + mydog.color)

neighbordog = Dog()
neighbordog.name = "Lisa"
print(mydog.name + " and " + neighbordog.name + " hate each other! ")

mydog.Bark()
neighbordog.Bark()


