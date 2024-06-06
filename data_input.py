from Main_file import Characters

def main(): 
 print("Be part of us") 
 print("It's important to be counted") 
 print("Fill in the document below") 

     
name = input("Enter your name: ") 
date_of_birth = input("Enter your date of birth (YYYY-MM-DD): ") 
character = Characters(name, date_of_birth) 
parents = input("The name of the parents:")
height = input("What is your height? (cm) :") 

     



 

def ask_parents(character): 
    if not isinstance(character, Characters): 
        raise TypeError("You must insert at least two parents") 

    parents = input("What are your parents' names? ") 
    return parents 

 

def ask_height(character): 
    height = input("Enter your height: ") 
    return height 

 

def display(character, height, parents, name, date_of_birth): 
    return (f"Name: {name}, DOB: {date_of_birth}, " 
            f"Height: {height}, Parents: {parents}") 

 
def save_to_file(Project_storage, content): 
    with open(Project_storage, 'w') as file: 
        file.write(content) 

def print_file_content(Project_storage): 

    with open(Project_storage, 'r') as file: 
        content = file.read() 
    print(content) 

 

content = display(character, height, parents) 
save_to_file('Project storage', content) 

print_file_content('project storage.txt') 



if __name__ == "__main__": 
    main() 

 

 