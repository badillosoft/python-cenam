import math

class Robot:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def avanzar(self, d, a):
        self.x += d * math.cos(a * math.pi / 180)
        self.y += d * math.sin(a * math.pi / 180)
    def info(self):
        print("({:.2f}, {:.2f})".format(self.x, self.y))
        
class RobotC3P0(Robot):
    def walkSquare(self):
        self.avanzar(1, 0)
        self.info()
        self.avanzar(1, 90)
        self.info()
        self.avanzar(1, 180)
        self.info()
        self.avanzar(1, 270)
        self.info()