class Characters:
    def __init__ (self, name, date_of_Birth):
        self.name=name
        self.date_of_Birth=date_of_Birth
        






class Humans(Characters):
    def __init__ (self,height,age,eye_colour, nationality,):
        
        self.height=height
        self.age=age
        self.eye_colour=eye_colour
        self.nationality=nationality
        self.GrandParents = False
        self.Parents = False
        

    def add_Parents(self):
        self.Parents = True
    

    def add_GrandParents(self):
        self.GrandParents = True

    def __str__(self):
        return f"Name: {self.name}, DOB: {self.date_of_birth}, Colour: {self.colour}, Type: {self.animal_type}, Breed: {self.breed}"



        


class Animals(Characters):
    def __init__ (self, colour, type, breed):  
        
        self.colour=colour
        self.type=colour
        self.breed = breed
        
    def __str__(self):
        return f"Name: {self.name}, DOB: {self.date_of_birth}, Colour: {self.colour}, Type: {self.animal_type}, Breed: {self.breed}"

def count_humans_and_animals(Characters):
     Characters = Characters.lower()
     humans_count = Characters.count("people")
     animals_count = Characters.count("animals")
     return humans_count, animals_count    






