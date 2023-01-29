class Car:
    def __init__(self, **kwargs):
        self.make = kwargs["make"]
        # self.model = kwargs["model"]
        # the benifit of the get() is that if the value doesn't exist in the passed arguments it return "None" and doesn't give any error
        self.model = kwargs.get("model")
        self.colour = kwargs.get("colours")
        self.seats = kwargs.get("seats")


my_car = Car(make="Nissan", model="GT-R")
my_car2 = Car(make="Nissan", colour="gray")
print(my_car.model)
print(my_car.make)
################
print(my_car2.model)
print(my_car2.colour)
