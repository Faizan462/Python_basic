# class Vehical ():
#     Brand = "Toyota"
#     def __init__(self , type , name , model):
#         self.type = type
#         self.name = name
#         self.model = model
#         print ("Vehical Created")


# v1 = Vehical("sudan" , "Corolla" , 2020)
# print(v1.Brand , v1.type , v1.name , v1.model)
# v2 = Vehical("sudan" , "Camry" , 2021)
# print(v2.Brand , v2.type , v2.name , v2.model)
# v3 = Vehical("suv" , "land Cruiser" , 2022)
# print(v3.Brand , v3.type , v3.name , v3.model)




# class Vehicle:
#     def __init__(self, brand, speed):
#         self.brand = brand        
#         self.__speed = speed      

#     def get_speed(self):
#         return self.__speed

#     def set_speed(self, speed):
#         self.__speed = speed


# car = Vehicle("Toyota", 120)

# print("Brand:", car.brand)
# print("Speed:", car.get_speed())

# car.set_speed(150)
# print("New Speed:", car.get_speed())




# class Vehicle:
#     def start(self):
#         print("Vehicle Started")


# class Car(Vehicle):
#     def drive(self):
#         print("Car is Driving")


# obj = Car()

# obj.start()      
# obj.drive()      





# class Vehicle:
#     def sound(self):
#         print("Vehicle makes a sound")


# class Car(Vehicle):
#     def sound(self):
#         print("Car says Beep Beep")


# class Bike(Vehicle):
#     def sound(self):
#         print("Bike says Vroom")


# c = Car()
# b = Bike()

# c.sound()
# b.sound()







from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def fuel_type(self):
        pass


class Car(Vehicle):

    def fuel_type(self):
        print("Car uses Petrol")


obj = Car()
obj.fuel_type()