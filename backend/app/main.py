import csv
import logging

from fastapi import FastAPI, Depends

from sqlalchemy import inspect
from sqlalchemy.orm import Session

from app.db.database import SessionLocal, engine
from app.domain import models
from app.domain.models import Meteorite

from typing import List


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

def tables_have_data(engine):
    inspector = inspect(engine)
    table_names = inspector.get_table_names()

    for table_name in table_names:
        # Check if the table has any rows
        result = engine.execute(f"SELECT COUNT(*) FROM {table_name}")
        row_count = result.scalar()

        if row_count > 0:
            # The table has data
            return True

    # No table has data
    return False

# Function to insert data into the database
def insert_data(db: Session, data: List):
    # Create and add instances of the Meteorite class for each data entry
    for entry in data:
        try:
            # Clean up the entry by removing unwanted characters
            cleaned_entry = entry[0].strip('[').strip(']').replace(';;', '')
            cleaned_entry = cleaned_entry.split(',')

            # Extract the geolocation separately
            geolocation = cleaned_entry[-1].strip('"')

            # Replace empty strings with None for nullable fields
            cleaned_entry = [field if field !=
                             '' else None for field in cleaned_entry]

            meteorite = Meteorite(
                name=cleaned_entry[0],
                idMeteorite=int(
                    cleaned_entry[1]) if cleaned_entry[1] else None,
                nametype=cleaned_entry[2],
                recclass=cleaned_entry[3],
                mass=float(cleaned_entry[4]) if cleaned_entry[4] else None,
                fall=cleaned_entry[5],
                year=int(cleaned_entry[6]) if cleaned_entry[6] else None,
                reclat=float(cleaned_entry[7]) if cleaned_entry[7] else None,
                reclong=float(cleaned_entry[8]) if cleaned_entry[8] else None,
                geolocation=geolocation,
            )

            logger.info("Inserting meteorite: %s", meteorite)
            db.add(meteorite)
        except Exception as e:
            logger.error("Error processing entry: %s", cleaned_entry)
            logger.error("Error details: %s", str(e))
            continue
    db.commit()


# Asynchronous event handler for startup
async def startup_event():
    db = SessionLocal()
    try:
        # Check if tables have data
        if not tables_have_data(engine):
            logger.info("Tables are empty. Initializing data.")
            
            # Read data from CSV file
            with open(csv_file_path, newline='', encoding='utf-8') as csvfile:
                csv_reader = csv.reader(csvfile, delimiter=',', quotechar='"')
                # Skip the header if present
                next(csv_reader, None)
                data = list(csv_reader)

                # Insert data into the database
                insert_data(db, data)
        else:
            logger.info("Tables have data. Skipping data initialization.")
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
