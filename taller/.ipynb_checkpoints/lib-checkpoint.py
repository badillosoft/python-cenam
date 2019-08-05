class Buffer:
    def __init__(self, MAX, *values):
        self.MAX = MAX
        self.buffer = list(values)[-MAX:]
    def accum(self, value):
        if len(self.buffer) >= self.MAX:
            self.buffer.pop(0)
        self.buffer.append(value)
    def reset(self):
        self.buffer = []
    def fill(self, value):
        while len(self.buffer) < self.MAX:
            self.buffer.append(value)
    def full(self, value):
        self.buffer = [value] * self.MAX
    def isEmpty(self):
        return len(self.buffer) == 0
    def isFull(self):
        return len(self.buffer) == self.MAX
    def __str__(self):
        s1 = "E" if self.isEmpty() else "!E"
        s2 = "F" if self.isFull() else "!F"
        return "Buffer: {} {} {}".format(self.buffer, s1, s2)
    
import math
import time

class InstrumentoSim:
    def read(self):
        return math.cos(time.time())