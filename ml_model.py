def predict_health_efficiency(data):
    # For simplicity, let's say efficiency is based on HeartRate and BodyTemperature
    heart_rate_avg = data['HeartRate'].mean()
    body_temp_avg = data['BodyTemperature'].mean()
    
    # Simple logic for prediction (you can replace this with a real ML model)
    if heart_rate_avg > 90 or body_temp_avg > 38:
        efficiency = 'Low'
    elif 70 < heart_rate_avg <= 90 and 37 < body_temp_avg <= 38:
        efficiency = 'Moderate'
    else:
        efficiency = 'High'

    return efficiency
