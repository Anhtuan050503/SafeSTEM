from fastapi import FastAPI

from backend.app.api.user import router as user_router
from backend.app.database.database import test_database_connection
from backend.app.api.lego_kit import router as lego_kit_router
from backend.app.api.lego_part import router as lego_part_router
from backend.app.api.kit_part import router as kit_part_router

app = FastAPI(
    
    title="SafeSTEM Vision API",
    description="Backend API for SafeSTEM Vision",
    version="1.0.0"
)

app.include_router(user_router)

app.include_router(lego_kit_router)
app.include_router(lego_part_router)
app.include_router(kit_part_router)

@app.get("/")
def root():
    return {
        "message": "SafeSTEM Vision API is running"
    }


@app.get("/health")
def health_check():
    return {
        "status": "OK"
    }


@app.get("/health/database")
def database_health():
    try:
        test_database_connection()

        return {
            "status": "OK",
            "database": "MySQL",
            "message": "Connected to safestem_db"
        }

    except Exception as e:
        return {
            "status": "ERROR",
            "message": str(e)
        }