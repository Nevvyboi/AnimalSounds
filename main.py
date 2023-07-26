 
class Animal:
    
    def make_sound(self):
        print("Mooooooo!")
        
class Dog(Animal):
    def __init__(self):
        self.animalSound = "Woof Woof!"
    
    def make_sound(self):
        super().make_sound()
        print(self.animalSound)
    
class Cat(Animal):
    def __init__(self):
        self.animalSound = "Meow Meow!"
        
    def make_sound(self):
        super().make_sound()
        print(self.animalSound)
    
if __name__ == "__main__":
    dog = Dog()
    cat = Cat()
    dog.make_sound()
    cat.make_sound()
