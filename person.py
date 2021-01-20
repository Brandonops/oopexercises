class Person:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone
        self.friends = [] #added an empty friends list
        self.greeting_count = 0 #added greeting count attribute and set it to 0

    def add_friend(self, other_person): #adding friends method
        self.friends.append(other_person) #adding friend to list of friends
    
    def num_friends(self):  #counting number of friends method
        return print(len(self.friends)) #returning number of friends

    def print_contact_info(self):
        print("---------------------")
        print(f"{self.name}'s' contact info is: \nemail: {self.email} \nPhone: {self.phone}")
        print("---------------------")
        
    def greet(self, other_person):
        print(f"Hello {other_person.name}, I am {self.name}!")
        self.greeting_count += 1
        return self.greeting_count
        ### need help with greet_count

    def __str__(self):
        return (f"Name: {self.name} \nContact info is: \nEmail: {self.email} \nphone: {self.phone}")


sonny = Person("Sonny", "sonny@hotmail.com.email",  "483-485-4948")
jordan = Person("Jordan", "jordan@aol.com", "495-586-3456")

sonny.greet(jordan)
jordan.greet(sonny)

jordan.add_friend(sonny)
jordan.num_friends()

print(jordan)
print(sonny)

class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
   
    def print_info(self):
        print(f"Vehicle's Info: \n{self.year} {self.make} {self.model}")

car = Vehicle("Nissan", "Leaf", 2015)
car.print_info()
