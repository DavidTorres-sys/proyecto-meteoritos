import logging

from fastapi import FastAPI, Depends

from sqlalchemy.orm import Session

from app.utils.initialization import init_data_on_startup
from app.services.crud.tables_data import get_tables_have_data
from app.db.database import SessionLocal, engine
from app.domain import models


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

csv_file_path = "app/db/meteorite-landings/meteorite.csv"

# Create tables if they do not exist
models.Base.metadata.create_all(bind=engine)

# Create FastAPI app instance
app = FastAPI()

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

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


# Root endpoint
@app.get("/")
async def root(db: Session = Depends(get_db)):
    return {"message": "Hello World"}
