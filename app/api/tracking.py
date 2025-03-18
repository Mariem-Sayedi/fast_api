from fastapi import APIRouter, HTTPException
from app.models import Event
from app.storage import save_event, get_all_events

router = APIRouter()

@router.post("/track", status_code=201)
async def track_event(event: Event):
    """Suivre un événement utilisateur (ajout au panier, vue, achat...)"""
    try:
        save_event(event.model_dump()) 
        return {"status": "success", "message": "Event tracked successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error tracking event: {str(e)}")

@router.get("/events")
async def get_events():
    """Obtenir tous les événements enregistrés"""
    try:
        events = get_all_events()
        return {"status": "success", "events": events}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error retrieving events: {str(e)}")
