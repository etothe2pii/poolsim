from dataclasses import dataclass, field


@dataclass
class Ball:
    start_position: tuple
    velocity: tuple
    in_pocket: bool = False
    diameter: float = 2.25
    mass: float = 0.17
    crr: float = 0.1
    normal_force: float = field(init=False)
    friction: float =  field(init=False)
    acceleration: float = field(init=False)

    def __post_init__(self):
        self.normal_force = self.mass * 9.8
        self.friction = self.normal_force * self.crr
        self.acceleration = 9.8*self.crr

    def get_position(self, time) -> tuple:
        



@dataclass
class Table:
    balls: list[Ball]
    dimensions: tuple[float] = (78.0, 39.0)

@dataclass
class Collision:
    time: float
    b1: Ball
    b2: Ball