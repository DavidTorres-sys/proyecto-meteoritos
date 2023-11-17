# main file (e.g., app/main.py)
from fastapi import FastAPI
from app.services.crud.tables_data import get_tables_have_data
from app.utils.initialization import init_data_on_startup
from app.utils.database import get_db, logger  # Import the get_db function and logger
from app.db.database import SessionLocal, engine
from app.api.endpoints import meteorite
from app.domain import models

# Create tables if they do not exist
models.Base.metadata.create_all(bind=engine)

# Create FastAPI app instance
app = FastAPI()

# Dependency to get the database session
app.dependency_overrides[get_db] = get_db

# Asynchronous event handler for startup
async def startup_event():
    db = SessionLocal()
    try:
        if not get_tables_have_data(engine):
            init_data_on_startup(db)
        else:
            logger.info("Data already exists in the database")
    except Exception as e:
        logger.error("Error during startup: %s", str(e))
    finally:
        db.close()

# Register the event handler with FastAPI
app.add_event_handler("startup", startup_event)

app.include_router(meteorite.router, prefix="/api/v1", tags=["meteorite"])
