from turtle import Turtle
from random import choice, randint


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_cars(self):
        chance = randint(1,6)
        if chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(1, 2)
            new_car.penup()
            new_car.color(choice(COLORS))
            new_car.goto(300, randint(-220, 220))
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def speedUP(self):
        self.car_speed += MOVE_INCREMENT
