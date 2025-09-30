class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
    
    def introduce(self):
        print(f"My name is {self.name}, I am {self.age} years old, studying {self.grade}.")

# Create objects
s1 = Student("Sameer", 21, "degree")
s2 = Student("Kausar", 17, "12+")

s1.introduce()
s2.introduce()


class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    
    def book_info(self):
        print(f"'{self.title}' by {self.author}, {self.pages} pages.")

# Objects
b1 = Book("Harry Potter", "J.K. Rowling", 500)
b2 = Book("THE 48 LAWS OF POWER", "Robert Greene", 480)

b1.book_info()
b2.book_info()



