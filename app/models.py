#Définition des classes/modèles de données

from pydantic import BaseModel
from datetime import datetime

# Modèle pour un événement utilisateur
class Event(BaseModel):
    user_id: str
    product_id: str
    event_type: str  # "view", "add_to_cart", "purchase"
    timestamp: datetime = datetime.utcnow()
