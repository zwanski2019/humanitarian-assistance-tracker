
import random

class Migrant:
    def __init__(self, id, location):
        self.id = id
        self.location = location

    def move_randomly(self):
        self.location += random.uniform(-0.2, 0.2)
