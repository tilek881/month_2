class Animal:
    def __init__(self , name , age):
        self.name = name
        self.age = age

    def infos(self):
        return(f'NAME: {self.name} , AGE: {self.age} , BIRTH_YEAR: {2024 - self.age}')


some_animal = Animal ('Anim' , 9)  
print(some_animal.infos())      
some_animal.age = + 6