import pandas as pd
import random

def generate_health_data():
    # Generating random health data for demonstration purposes
    data = {
        'SoldierID': [f'S{random.randint(1, 100)}' for _ in range(10)],
        'HeartRate': [random.randint(60, 100) for _ in range(10)],
        'BodyTemperature': [round(random.uniform(36.5, 39.0), 1) for _ in range(10)],
        'RespirationRate': [random.randint(12, 20) for _ in range(10)],
    }
    df = pd.DataFrame(data)
    return df
