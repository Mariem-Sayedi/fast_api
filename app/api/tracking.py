from fastapi import APIRouter, HTTPException
from app.models import Event, SearchEvent
from app.storage import save_event, get_all_events, get_categories_viewed_by_user, save_search_query

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

@router.get("/categories-viewed/{user_id}")
async def get_categories_viewed(user_id: str):
    """Obtenir les sous-catégories niveau 1 et catégories niveau 2 vues par un client."""
    try:
        categories = get_categories_viewed_by_user(user_id)
        return {"status": "success", "categories": categories}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error retrieving categories: {str(e)}")
    

@router.post("/search", status_code=201)
async def track_search(search_event: SearchEvent):
    """Suivre les recherches effectuées par un utilisateur"""
    try:
        # Sauvegarde de l'événement de recherche
        save_search_query(search_event.model_dump()) 
        return {"status": "success", "message": "Search tracked successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error tracking search: {str(e)}")
