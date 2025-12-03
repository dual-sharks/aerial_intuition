from fastapi import FastAPI

from app.api_routes import router as api_router


app = FastAPI(title="NOAA API wrapper", version="0.1.0")
app.include_router(api_router)

