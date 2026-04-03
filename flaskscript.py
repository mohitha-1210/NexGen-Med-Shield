import serial
import time
from flask import Flask, jsonify
from flask_cors import CORS
import threading

app = Flask(__name__)
CORS(app)

# Global storage for the latest reading
pill_data = {"weight": "0", "result": "None", "status": "Waiting"}

def serial_listener():
    global pill_data
    try:
        # CHANGE 'COM3' TO YOUR PORT
        ser = serial.Serial('COM6', 9600, timeout=1)
        time.sleep(2) # Initial reset
        print("Connected to NexGen Hardware...")
        
        while True:
            if ser.in_waiting > 0:
                line = ser.readline().decode('utf-8').strip()
                print(f"Incoming: {line}")
                parts = line.split(',')
                if len(parts) == 3:
                    pill_data = {
                        "weight": parts[0],
                        "result": parts[1],
                        "status": "Scan Complete" if parts[2] == "2" else "Scanning"
                    }
    except Exception as e:
        print(f"Serial Error: {e}")

@app.route('/get-data')
def get_data():
    return jsonify(pill_data)

if __name__ == '__main__':
    threading.Thread(target=serial_listener, daemon=True).start()
    app.run(port=5000)
