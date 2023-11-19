import csv
import logging

from sqlalchemy.orm import Session
from app.services.crud.tables_data import get_tables_have_data
from app.db.database import engine
from app.utils.utils import *

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def init_data_on_startup(db: Session):
    try:
        if not get_tables_have_data(engine):
            with open("app/db/earthquakes_data/earthquakes.csv", newline='', encoding='utf-8') as csvfile:
                csv_reader = csv.reader(csvfile, delimiter=',', quotechar='"')
                data = list(csv_reader)
                for entry in data:
                    try:
                        clean_data = parse_csv_entry(entry)
                        earthquake = create_earthquake_object(clean_data)
                        location = create_location_object(clean_data)
                        magnitude = create_magnitude_object(clean_data)
                        source = create_source_object(clean_data)
                        status = create_status_object(clean_data)
                        # Add objects to the session without committing
                        db.add(earthquake)
                        db.add(location)
                        db.add(magnitude)
                        db.add(source)
                        db.add(status)
                        # Commit the session to generate IDs
                        db.commit()
                        # Assign IDs to related objects
                        location.earthquake_id = earthquake.id
                        magnitude.earthquake_id = earthquake.id
                        source.earthquake_id = earthquake.id
                        status.earthquake_id = earthquake.id
                        # Commit again to persist the relationships
                        db.commit()
                        logger.info("Adding earthquake: %s", earthquake)
                    except Exception as e:
                        logger.error("Error adding earthquake: %s", str(e))
                        db.rollback()
                        continue
    except Exception as e:
        logger.error("Error during data initialization: %s", str(e))
