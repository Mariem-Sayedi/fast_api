#Définition des classes/modèles de données

from pydantic import BaseModel
from datetime import datetime

# Modèle pour un événement utilisateur
class Event(BaseModel):
    user_id: str
    product_id: str
    subcategory: str
    category: str 
    event_type: str  # "view", "add_to_cart", "purchase"
    timestamp: datetime = datetime.utcnow()


# Modèle pour une recherche utilisateur
class SearchEvent(BaseModel):
    user_id: str        
    search_query: str   
    timestamp: datetime = datetime.utcnow()