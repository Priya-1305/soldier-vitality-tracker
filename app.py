from flask import Flask, jsonify, request
import random
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "http://localhost:3000"}})

# Function to generate realistic health data based on conditions
def generate_health_data(condition, soldier_profile):
    if condition == 'rest':
        # Simulate resting state metrics
        heart_rate = random.randint(60, 80)
        body_temp = round(random.uniform(36.5, 37.0), 1)
        respiration_rate = random.randint(12, 16)
        oxygen_level = random.randint(95, 100)
        blood_pressure = (random.randint(110, 120), random.randint(70, 80))

    elif condition == 'stress':
        # Simulate stressed state metrics
        heart_rate = random.randint(90, 110)
        body_temp = round(random.uniform(37.0, 37.8), 1)
        respiration_rate = random.randint(18, 22)
        oxygen_level = random.randint(90, 95)
        blood_pressure = (random.randint(120, 130), random.randint(80, 85))

    elif condition == 'exertion':
        # Simulate physical exertion metrics
        heart_rate = random.randint(120, 160)
        body_temp = round(random.uniform(37.2, 38.0), 1)
        respiration_rate = random.randint(25, 35)
        oxygen_level = random.randint(90, 95)
        blood_pressure = (random.randint(130, 140), random.randint(85, 90))

    return {
        'SoldierID': soldier_profile['SoldierID'],
        'HeartRate': heart_rate,
        'BodyTemperature': body_temp,
        'RespirationRate': respiration_rate,
        'OxygenSaturation': oxygen_level,
        'BloodPressure': blood_pressure
    }

# Sample soldier profiles
soldier_profiles = [
    {"SoldierID": "S42", "Condition": "rest"},
    {"SoldierID": "S71", "Condition": "stress"},
    {"SoldierID": "S19", "Condition": "exertion"}
]

# Flask route to serve soldier data
@app.route('/api/soldier_data', methods=['GET'])
def get_soldier_data():
    soldier_data = []
    for soldier in soldier_profiles:
        data = generate_health_data(soldier["Condition"], soldier)
        soldier_data.append(data)
    
    return jsonify(soldier_data)

# Flask route to update soldier condition
@app.route('/api/update_condition', methods=['POST'])
def update_soldier_condition():
    data = request.json
    soldier_id = data.get('SoldierID')
    new_condition = data.get('Condition')

    # Update the soldier's condition in the profiles
    for soldier in soldier_profiles:
        if soldier["SoldierID"] == soldier_id:
            soldier["Condition"] = new_condition
            return jsonify({"message": f"Condition updated for soldier {soldier_id}."}), 200
    
    return jsonify({"error": "Soldier not found."}), 404

if __name__ == '__main__':
    app.run(debug=True)
