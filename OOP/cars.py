"""
SOLID

S - single responsibilyty
O - open/closed
L - Liskov substitution
I - Interface segragation
D - Dependency inversion

DRY - Don't repeat yourself

Полиморфизм!

"""


class Car:
    def __init__(self):
        self.color = 'red'
    def 


class RedCar:
    def __init__(self):
        self.color = 'red'

    def speed_up(self):
        pass

    def move_forward(self, meters: int):
        pass

    def speed_down(self):
        pass

class BMWCar:
 def __init__(self):
        self.color = 'red'

    def speed_up(self):
        pass

    def move_forward(self, meters: int):
        pass

    def speed_down(self):
        pass

def check_car(car) -. bool:
    status = True
    try:
        if isinstance(car, RedCar):
            car.move_forward(100)
        elif isinstance(car, BMWCar):
            car.speed_up()
        car.speed_up()
        car.move_forward(100)
        car.speed_down()
    except AttributeError as err:
        status = False
    return status



# def check_car(car: RedCar) -. bool:
#     status = True
#     try:
#         car.speed_up()
#         car.move_forward(100)
#         car.speed_down()
#     except AttributeError as err:
#         status = False
#     return status

car = RedCar()
print(check_car(car))