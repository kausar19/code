#there are 2 types of constructors in python 
# * default construyctor (without arguments)
# *parameterized constructor (with arguments - most common)
# * python does not support multiple constructors
class Demo:
    def __init__(self):
        print("Default constructor called!")

obj = Demo()
class Demo:
    def __init__(self, name="Unknown", age=0):
        self.name = name
        self.age = age

d1 = Demo("Kausar", 17)   # passes both
d2 = Demo("Hiba"  , 17)       # age default = 0
d3 = Demo()               # name="Unknown", age=0

print(d1.name, d1.age)
print(d2.name, d2.age)
print(d3.name, d3.age)
