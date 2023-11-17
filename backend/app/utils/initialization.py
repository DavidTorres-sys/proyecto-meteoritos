import csv
import logging

from sqlalchemy import update, func
from app.domain.models import Meteorite
from sqlalchemy.orm import Session
from app.services.crud.tables_data import get_tables_have_data
from app.db.database import engine
from app.utils.utils import parse_csv_entry, create_meteorite_object

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def init_data_on_startup(db: Session):
    try:
        if not get_tables_have_data(engine):
            # Read data from CSV file
            with open("app/db/meteorite-landings/meteorite.csv", newline='', encoding='utf-8') as csvfile:
                csv_reader = csv.reader(csvfile, delimiter=',', quotechar='"')
                data = list(csv_reader)
                for entry in data:
                    try:
                        cleaned_entry = parse_csv_entry(entry)
                        meteorite = create_meteorite_object(cleaned_entry)
                        logger.info("Adding meteorite: %s", meteorite)
                        db.add(meteorite)
                        db.commit()
                    except Exception as e:
                        logger.error("Error adding meteorite: %s", str(e))
                        db.rollback()
                        continue
    except Exception as e:
        logger.error("Error during data initialization: %s", str(e))


        
