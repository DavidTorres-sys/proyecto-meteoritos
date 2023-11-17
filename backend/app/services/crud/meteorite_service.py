import pandas as pd
from geopy.geocoders import Nominatim
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut, GeocoderServiceError

from sklearn.preprocessing import LabelEncoder

from app.db.database import SessionLocal

from sqlalchemy.orm import Session
from .meteorite_crud import meteorite_crud
from app.domain.models import Meteorite


def get_characteristics():
    meteorites = SessionLocal().query(Meteorite).all()

    # Convert the data to a DataFrame
    df = pd.DataFrame([m.__dict__ for m in meteorites])

    # Drop non-numeric columns and handle missing values
    df = df.drop(["id", "name"], axis=1)
    df = df.dropna()

    # Encode categorical variables
    le = LabelEncoder()
    df["fall"] = le.fit_transform(df["fall"])

    return df


def get_meteorite(db: Session, meteorite_id: int):
    return meteorite_crud.read(db, meteorite_id)


def get_meteorites(db: Session, skip: int = 0, limit: int = 100):
    return meteorite_crud.read_all(db, skip=skip, limit=limit)


def analyze_mass_distribution(df):
    fell_meteorites = df[df['fall'] == 1]
    found_meteorites = df[df['fall'] == 0]

    return {
        "fell": {"mean": fell_meteorites['mass'].mean(), "std": fell_meteorites['mass'].std()},
        "found": {"mean": found_meteorites['mass'].mean(), "std": found_meteorites['mass'].std()}
    }


def analyze_class_distribution(df):
    fell_meteorites = df[df['fall'] == 1]
    found_meteorites = df[df['fall'] == 0]

    return {
        "fell": fell_meteorites['recclass'].value_counts().to_dict(),
        "found": found_meteorites['recclass'].value_counts().to_dict()
    }


def analyze_location_distribution(df):
    fell_meteorites = df[df['fall'] == 1]
    found_meteorites = df[df['fall'] == 0]

    return {
        "fell": {"mean_lat": fell_meteorites['reclat'].mean(), "mean_long": fell_meteorites['reclong'].mean()},
        "found": {"mean_lat": found_meteorites['reclat'].mean(), "mean_long": found_meteorites['reclong'].mean()}
    }


def analyze_class(df):
    recclass = df['recclass'].value_counts().to_dict()
    return recclass


def get_continent_from_coordinates(meteorite_id: int):
    meteorite = get_meteorite(SessionLocal(), meteorite_id)
    geolocator = Nominatim(user_agent="app")
    try:
        location = geolocator.reverse(f"{meteorite.reclat}, {meteorite.reclong}")
        return location.raw['address']['continent']
    except (GeocoderTimedOut, GeocoderServiceError):
        return None
