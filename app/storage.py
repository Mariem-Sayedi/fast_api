# Gestion du stockage (fichier CSV)

import pandas as pd
import os

EVENTS_CSV_FILE = "data/events.csv"
SEARCH_CSV_FILE = "data/search.csv"

 
if not os.path.exists(EVENTS_CSV_FILE):
    df = pd.DataFrame(columns=["user_id", "product_id", "subcategory", "category", "event_type", "timestamp", "\n\t"])
    df.to_csv(EVENTS_CSV_FILE, index=False)

if not os.path.exists(SEARCH_CSV_FILE):
    df = pd.DataFrame(columns=["user_id", "search_query", "timestamp", "\n\t"])
    df.to_csv(SEARCH_CSV_FILE, index=False)


def save_event(event: dict):
    new_data = pd.DataFrame([event]) 
    new_data.to_csv(EVENTS_CSV_FILE, mode="a", header=False, index=False) 

def get_all_events():
    return pd.read_csv(EVENTS_CSV_FILE).to_dict(orient="records")

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

def save_search_query(search_query: dict):
    new_data = pd.DataFrame([search_query]) 
    new_data.to_csv(SEARCH_CSV_FILE, mode="a", header=False, index=False) 
