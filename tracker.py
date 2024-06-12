
from drone import Drone
from migrant import Migrant
import json

def track_migrants(drones, migrants):
    for drone in drones:
        for migrant in migrants:
            if is_nearby(drone.location, migrant.location):
                print(f"Drone {drone.id} has detected migrant {migrant.id} at location {migrant.location}")

def is_nearby(location1, location2, threshold=1.0):
    return abs(location1 - location2) <= threshold

def save_state(drones, migrants, filename='state.json'):
    state = {
        'drones': [{'id': drone.id, 'location': drone.location} for drone in drones],
        'migrants': [{'id': migrant.id, 'location': migrant.location} for migrant in migrants]
    }
    with open(filename, 'w') as f:
        json.dump(state, f)

def load_state(filename='state.json'):
    with open(filename, 'r') as f:
        state = json.load(f)
    drones = [Drone(**drone) for drone in state['drones']]
    migrants = [Migrant(**migrant) for migrant in state['migrants']]
    return drones, migrants
# tracker.py
from drone import Drone
from migrant import Migrant
import json

def track_migrants(drones, migrants):
    for drone in drones:
        for migrant in migrants:
            if is_nearby(drone.location, migrant.location):
                print(f"Drone {drone.id} has detected migrant {migrant.id} at location {migrant.location}")

def is_nearby(location1, location2, threshold=1.0):
    return abs(location1 - location2) <= threshold
