# Routes pour suivre les événements

from fastapi import APIRouter
from app.models import Event
from app.storage import save_event, get_all_events

router = APIRouter()

@router.post("/track")
async def track_event(event: Event):
    """Suivre un événement utilisateur (ajout au panier, vue, achat...)"""
    save_event(event.dict())  # Enregistrer l'événement dans le CSV
    return {"status": "success", "message": "Event tracked successfully"}

@router.get("/events")
async def get_events():
    """Obtenir tous les événements enregistrés"""
    return get_all_events()  # Récupérer tous les événements
