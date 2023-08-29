from dataclasses import dataclass, field
import math


@dataclass
class Ball:
    start_position: tuple
    velocity: tuple
    in_pocket: bool = False
    radius: float = 0.028575 #1.125 inches in meters
    mass: float = 0.17
    crr: float = 0.1 #Average coefficient of rolling resistance
    start_time: float = 0.0
    acceleration: tuple = field(init=False)


    def __post_init__(self):
        self.calculate_acceleration()

    def calculate_acceleration(self):
        acceleration = 9.8*self.crr*self.radius
        if self.velocity[1] == 0:
            angle = 0
        else:
            angle = math.atan(self.velocity[0]/self.velocity[1])
        x = math.sin(angle) * acceleration
        y = math.cos(angle) * acceleration

        self.acceleration = (x,y)

    #x = x_0 + v_0t + 0.5at^2
    # Assumes no velocity is lost at each collision (including with walls)
    # Does not account for walls in position estimate
    def get_position(self, time) -> tuple:
        time = time - self.start_time

        pos = tuple([p + v * time + 0.5 * a * (time ** 2) for p, v, a in zip(self.start_position, self.velocity, self.acceleration)])
        return pos

    # v = v_0 + at
    # Assumes no velocity is lost at each collision (including with walls)
    def get_velocity(self, time) -> tuple:
        time = time - self.start_time
        v = tuple([vel + time * acc for vel, acc in zip(self.velocity, acceleration)])

        return v
        



@dataclass
class Table:
    balls: list
    dimensions: tuple = (1.9812, 0.9906) #78 X 39 inches in meters

@dataclass
class Collision:
    time: float
    b1: Ball
    b2: Ball