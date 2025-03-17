# Gestion du stockage (fichier CSV)

import pandas as pd
import os

# Définir le fichier de stockage CSV
CSV_FILE = "data/events.csv"

# Créer le fichier CSV s'il n'existe pas
if not os.path.exists(CSV_FILE):
    df = pd.DataFrame(columns=["user_id", "product_id", "event_type", "timestamp"])
    df.to_csv(CSV_FILE, index=False)

# Fonction pour ajouter un événement
def save_event(event: dict):
    new_data = pd.DataFrame([event])  # Convertir l'événement en DataFrame
    new_data.to_csv(CSV_FILE, mode="a", header=False, index=False)  # Ajouter au fichier CSV

# Fonction pour récupérer tous les événements
def get_all_events():
    return pd.read_csv(CSV_FILE).to_dict(orient="records")
