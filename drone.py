
import random

class Drone:
    def __init__(self, id, location):
        self.id = id
        self.location = location

    def update_location(self, new_location):
        self.location = new_location

    def move_randomly(self):
        self.location += random.uniform(-0.5, 0.5)
