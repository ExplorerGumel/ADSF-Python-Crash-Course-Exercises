#9-1. Restaurant: Make a class called Restaurant. The __init__() method for 
#Restaurant should store two attributes: a restaurant_name and a cuisine_type. 
#Make a method called describe_restaurant() that prints these two pieces of 
#information, and a method called open_restaurant() that prints a message indicating 
#that the restaurant is open.Make an instance called restaurant from your class. 
#Print the two attributes individually, and then call both methods

class Restaurant:
    def __init__(self,name,cuisine):
        self.name = name
        self.cuisine = cuisine

    def describe_restaurant(self):
        print(f"The restaurant name is {self.name} and has {self.cuisine} type")

    def open_restaurant(self):
        print(f'The {self.name} Restaurant is opened')

my_restaurant = Restaurant('Elhabeb','Tuwon shinkafa')
print(my_restaurant.name)
print(my_restaurant.cuisine)
print(my_restaurant.describe_restaurant())
print(my_restaurant.open_restaurant())



##9-2. Three Restaurants: Start with your class from Exercise 9-1. Create three 
#different instances from the class, and call describe_restaurant() for each instance.

first_restaurant = Restaurant('El-Jalil','Doya')
second_restaurant = Restaurant('Glorious Hotel','Wake da Shinkafa')
third_restaurant = Restaurant('Mai Jama"a','Dan wake')

print(first_restaurant.describe_restaurant())
print(second_restaurant.describe_restaurant())
print(third_restaurant.describe_restaurant())





# 9-3. Users: Make a class called User. Create two attributes called first_name
#and last_name, and then create several other attributes that are typically stored 
#in a user profile. Make a method called describe_user() that prints a summary of 
#the user’s information. Make another method called greet_user() that prints a 
#personalized greeting to the user.Create several instances representing different 
#users, and call both methods for each user

class User:
    def __init__(self,first_name,last_name,age,nationality,gender):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.nationality = nationality
        self.gender = gender
    def describe_user(self):
        print(f"Name of the user is {self.first_name} {self.last_name} from {self.nationality}")
    def greet_user(self):
        print(f"Good morning {self.first_name} {self.last_name}")
        

first_user = User('Munzali','Alhassan',26,'Nigeria','Male')
print(first_user.describe_user())

second_user = User('Abubakar','Sani',26,'Nigeria','Male')
print(second_user.describe_user())

third_user = User('Aisha','Saleh',26,'Nigeria','Male')
print(third_user.describe_user())



class Restaurant:
    def __init__(self,name,cuisine):
        self.name = name
        self.cuisine = cuisine
        self.number_served = 0

    def describe_restaurant(self):
        print(f"The restaurant name is {self.name} and has {self.cuisine} type")

    def open_restaurant(self):
        print(f'The {self.name} Restaurant is opened')

    def set_number_served(self,people_served):
        self.number_served = people_served

    def increment_number_served(self,served):
        self.number_served += served

restaurant = Restaurant('Elhabeb','Tuwon shinkafa')
print(f"{restaurant.name} served {restaurant.number_served} people")

print('*' * 20)

restaurant.number_served = 12
print(f"{restaurant.name} served {restaurant.number_served} people")

print('*' * 20)

restaurant.set_number_served(30)
print(f"{restaurant.name} served {restaurant.number_served} people")

print('*' * 20)

restaurant.increment_number_served(70)
print(f"{restaurant.name} served {restaurant.number_served} people")



9-6. Ice Cream Stand: An ice cream stand is a specific kind of restaurant Write a class called IceCreamStand that inherits from the Restaurant class you wrote in Exercise 9-1 (page 162) or Exercise 9-4 (page 167). Either version of the class will work; just pick the one you like better. Add an attribute called flavors that stores a list of ice cream flavors. Write a method that displays these flavors. Create an instance of IceCreamStand, and call this method.



class Restaurant:
    def __init__(self,name,cuisine):
        self.name = name
        self.cuisine = cuisine

    def describe_restaurant(self):
        print(f"The restaurant name is {self.name} and has {self.cuisine} type")

    def open_restaurant(self):
        print(f'The {self.name} Restaurant is opened')

class IceCreamStand(Restaurant):
    def __init__(self, name, cuisine):
        super().__init__(name, cuisine)
        self.flavors = []
    def display_flavors(self,lst):
        self.flavors.append(lst)
        print(f"The flavors available are {self.flavors}")

my_icecream = IceCreamStand('Sauqi','Dambun Shinkafa')
print(my_icecream.display_flavors('juice'))





9-7. Admin: An administrator is a special kind of user. Write a class called 
Admin that inherits from the User class you wrote in Exercise 9-3 (page 162) 
or Exercise 9-5 (page 167). Add an attribute, privileges, that stores a list 
of strings like "can add post", "can delete post", "can ban user", and so on. 
Write a method called show_privileges() that lists the administrator’s set of 
privileges. Create an instance of Admin, and call your method

class User:
    def __init__(self,first_name,last_name,age,nationality):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.nationality = nationality
    def describe_user(self):
        print(f"Name of the user is {self.first_name} {self.last_name} aged {self.age} is from {self.nationality}")
    def greet_user(self):
        print(f"Good morning {self.first_name} {self.last_name}")

class Admin(User):
    def __init__(self, first_name, last_name, age, nationality):
        super().__init__(first_name, last_name, age, nationality)
        self.privileges = ["can add post", "can delete post", "can ban user"]
    def show_privileges(self):
        print(f"The user {self.first_name} {self.last_name} has the following privilages: {self.privileges}")
        

my_admin = Admin('Sani','Shehu',22,'Nigeria')
print(my_admin.show_privileges())



9-8. Privileges: Write a separate Privileges class. The class should have one 
attribute, privileges, that stores a list of strings as described in Exercise 9-7. 
Move the show_privileges() method to this class. Make a Privileges instance 
as an attribute in the Admin class. Create a new instance of Admin and use your 
method to show its privileges.

class User:
    def __init__(self,first_name,last_name,age,nationality):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.nationality = nationality
    def describe_user(self):
        print(f"Name of the user is {self.first_name} {self.last_name} aged {self.age} is from {self.nationality}")
    def greet_user(self):
        print(f"Good morning {self.first_name} {self.last_name}")

class Privileges:
    def __init__(self,privilege=["can add post", "can delete post", "can ban user"]):
        self.privilege = privilege
    def show_privileges(self):
        print(f"The user has the following privilages: {self.privilege}")
        

class Admin(User):
    def __init__(self, first_name, last_name, age, nationality):
        super().__init__(first_name, last_name, age, nationality)
        self.privilege = Privileges()

my_admin = Admin('Sani','Shehu',22,'Nigeria')
print(my_admin.privilege.show_privileges())



9-9. Battery Upgrade: Use the final version of electric_car.py from this section. 
Add a method to the Battery class called upgrade_battery(). This method 
should check the battery size and set the capacity to 100 if it isn’t already. 
Make an electric car with a default battery size, call get_range() once, and 
then call get_range() a second time after upgrading the battery. You should 
see an increase in the car’s range.

class Car:
 
 """A simple attempt to represent a car."""
 def __init__(self, make, model, year):
    self.make = make
    self.model = model
    self.year = year
    self.odometer_reading = 0
 
 def get_descriptive_name(self):
    long_name = f"{self.year} {self.make} {self.model}"
    return long_name.title()
 
 def read_odometer(self):
    print(f"This car has {self.odometer_reading} miles on it.")
 
 def update_odometer(self, mileage):
    if mileage >= self.odometer_reading:
        self.odometer_reading = mileage
    else:
        print("You can't roll back an odometer!")
 
 def increment_odometer(self, miles):
    self.odometer_reading += miles

class ElectricCar(Car):
 
 """Represent aspects of a car, specific to electric vehicles."""
 
 def __init__(self, make, model, year):
    super().__init__(make, model, year)
    self.battery_size = 75
 
 def describe_battery(self):
    print(f"This car has a {self.battery_size}-kWh battery.")
 
my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.read_odometer())
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()