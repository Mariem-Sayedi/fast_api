from fastapi import APIRouter, HTTPException
from app.storage import get_categories_viewed_by_user

router = APIRouter()


@router.get("/categories-viewed/{user_id}")
async def get_categories_viewed(user_id: str):
    """Obtenir les sous-catégories niveau 1 et catégories niveau 2 vues par un client."""
    try:
        categories = get_categories_viewed_by_user(user_id)
        return {"status": "success", "categories": categories}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error retrieving categories: {str(e)}")
    