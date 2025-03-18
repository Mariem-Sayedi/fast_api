# Gestion du stockage (fichier CSV)

import pandas as pd
import os

CSV_FILE = "data/events.csv"

 
if not os.path.exists(CSV_FILE):
    df = pd.DataFrame(columns=["user_id", "product_id", "event_type", "timestamp", "\n\t"])
    df.to_csv(CSV_FILE, index=False)

def save_event(event: dict):
    new_data = pd.DataFrame([event]) 
    new_data.to_csv(CSV_FILE, mode="a", header=False, index=False)  # Ajouter au fichier CSV

def get_all_events():
    return pd.read_csv(CSV_FILE).to_dict(orient="records")
