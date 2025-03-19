from fastapi import APIRouter, HTTPException
from app.models import SearchEvent
from app.storage import save_search_query

router = APIRouter()


@router.post("/search", status_code=201)
async def track_search(search_event: SearchEvent):
    """Suivre les recherches effectuées par un utilisateur"""
    try:
        save_search_query(search_event.model_dump()) 
        return {"status": "success", "message": "Search tracked successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error tracking search: {str(e)}")
    

