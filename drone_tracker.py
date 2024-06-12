
from drone import Drone
from migrant import Migrant
from tracker import track_migrants, save_state, load_state
import time

def main():
    drones = [Drone(id=1, location=0.0), Drone(id=2, location=5.0)]
    migrants = [Migrant(id=1, location=0.5), Migrant(id=2, location=6.0)]

    print("Tracking Migrants using Drones")
    
    try:
        while True:
            for drone in drones:
                drone.move_randomly()
            for migrant in migrants:
                migrant.move_randomly()
            track_migrants(drones, migrants)
            time.sleep(2)
    except KeyboardInterrupt:
        print("Saving state and exiting...")
        save_state(drones, migrants)

if __name__ == "__main__":
    main()
