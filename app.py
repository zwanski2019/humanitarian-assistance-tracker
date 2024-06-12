# app.py
from flask import Flask, render_template, jsonify, request
from drone import Drone
from migrant import Migrant
from tracker import track_migrants
import threading
import time

app = Flask(__name__)

drones = [Drone(id=1, location=0.0), Drone(id=2, location=5.0)]
migrants = [Migrant(id=1, location=0.5), Migrant(id=2, location=6.0)]
tracking = False
tracking_thread = None

def track():
    global tracking
    while tracking:
        for drone in drones:
            drone.move_randomly()
        for migrant in migrants:
            migrant.move_randomly()
        track_migrants(drones, migrants)
        time.sleep(2)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start')
def start_tracking():
    global tracking, tracking_thread
    if not tracking:
        tracking = True
        tracking_thread = threading.Thread(target=track)
        tracking_thread.start()
    return jsonify({"status": "started"})

@app.route('/stop')
def stop_tracking():
    global tracking
    if tracking:
        tracking = False
        tracking_thread.join()
    return jsonify({"status": "stopped"})

@app.route('/status')
def status():
    drones_data = [{'id': drone.id, 'location': drone.location} for drone in drones]
    migrants_data = [{'id': migrant.id, 'location': migrant.location} for migrant in migrants]
    return jsonify({"drones": drones_data, "migrants": migrants_data})

if __name__ == "__main__":
    app.run(debug=True)
