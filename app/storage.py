# Gestion du stockage (fichier CSV)

import pandas as pd
import os

CSV_FILE = "data/events.csv"

 
if not os.path.exists(CSV_FILE):
    df = pd.DataFrame(columns=["user_id", "product_id", "subcategory", "category", "event_type", "timestamp", "\n\t"])
    df.to_csv(CSV_FILE, index=False)

def save_event(event: dict):
    new_data = pd.DataFrame([event]) 
    new_data.to_csv(CSV_FILE, mode="a", header=False, index=False) 

def get_all_events():
    return pd.read_csv(CSV_FILE).to_dict(orient="records")

def get_categories_viewed_by_user(user_id: str):
    """Retourne les sous-catégories et catégories vues par un utilisateur."""
    events = get_all_events()
    print("events", events)
    categories = set()

    for event in events:
        if str(event["user_id"]) == str(user_id) and event["event_type"] == "view":
          categories.add((event["subcategory"], event["category"]))
          print("categories", categories)
    return list(categories)

