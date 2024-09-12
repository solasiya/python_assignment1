class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    
    def introduce(self):
        print(f"Hello, I'm {self.name}. I'm {self.age} years old and I identify as {self.gender}.")

# Create an instance of the Person class
Person = Person("Amahle Zungu", 28, "female")

# Call the introduce method
Person.introduce()