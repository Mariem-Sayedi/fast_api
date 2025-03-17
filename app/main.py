#point d'entrée pour l'api
from fastapi import FastAPI
from app.api.tracking import router

app = FastAPI()

# Inclure le routeur des événements
app.include_router(router)
