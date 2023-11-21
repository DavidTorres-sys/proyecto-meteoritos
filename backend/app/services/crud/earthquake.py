# Standard Library Imports
from sqlalchemy.sql import func

# Third-Party Imports
from sqlalchemy.orm import Session, selectinload
from geopy.distance import geodesic
# from sklearn.neighbors import KDTree
# import numpy as np

# Local Imports
from app.domain.models import Earthquake, LocationEarthquake
from app.domain.schemas import (
    EarthquakeResponse, MagnitudeResponse, SourceResponse, StatusResponse)
from app.domain.schemas.location_earthquake import LocationEarthquakeResponse
from app.core.thresholds import thresholds, suggested_actions, factors
from app.core.constants import (
    HOUSING_TYPE_APARTMENT,
    SUGGESTION_HOUSING_TYPE,
    SUGGESTION_EMERGENCY_RESOURCES,
    SUGGESTION_EVACUATION_PLAN,
    SUGGESTION_EXPERIENCE_EMERGENCY,
    SUGGESTION_MEDICAL_CONDITIONS,
    SUGGESTION_PARTICIPATION_DRILLS,
    SUGGESTION_COMMUNICATION_DEVICE
)
from .earthquake_crud import *


def get_earthquake(db: Session, meteorite_id: int):
    return earthquake_crud.read(db, meteorite_id)


def get_earthquakes(db: Session, skip: int = 0, limit: int = 100):
    return earthquake_crud.read_all(db, skip=skip, limit=limit)


def get_earthquake_data(db: Session, user_latitude: float, user_longitude: float):
    user_point = func.ST_GeomFromText(
        f'POINT({user_longitude} {user_latitude})', 4326)

    earthquakes_query = (
        db.query(Earthquake)
        .join(LocationEarthquake, Earthquake.id == LocationEarthquake.earthquake_id)
        .options(selectinload(Earthquake.location_earthquake))
        .filter(
            func.ST_DWithin(user_point, LocationEarthquake.geom, 50 * 1000),
        )
        .limit(10)
        .all()
    )

    return earthquakes_query


def calculate_magnitude_factor(earthquake_data):
    """
    Returns a factor based on the maximum magnitude of earthquakes within 500 km of the user's location.
    Parameters:
        earthquake_data (list): List of earthquake data
    returns:
        Factor based on the maximum magnitude of earthquakes within 500 km of the user's location"""
    max_magnitude = max(
        [quake.magnitude.value for quake in earthquake_data], default=0)
    return max_magnitude * 0.1


def calculate_distance_factor(earthquake_data, user_latitude, user_longitude):
    """
    Returns a factor based on the closest distance of an earthquake within 500 km of the user's location.
    Parameters:
        earthquake_data (list): List of earthquake data
        user_latitude (float): User's latitude
        user_longitude (float): User's longitude
    returns:
        Factor based on the closest distance of an earthquake within 500 km of the user's location"""
    closest_distance = min([geodesic((user_latitude, user_longitude), (quake.location_earthquake.latitude,
                           quake.location_earthquake.longitude)).kilometers for quake in earthquake_data], default=0)
    return 1 / (closest_distance + 1)


def calculate_earthquake_probability(user_latitude, user_longitude, model_answers):
    """
    Returns the probability of an earthquake occurring based on the user's location and answers to the form.
    Parameters:
        user_latitude (float): User's latitude
        user_longitude (float): User's longitude
        model_answers (dict): User's answers to the form
    returns:
        Probability of an earthquake occurring
    """
    earthquake_data = get_earthquake_data(user_latitude, user_longitude)

    factors_sum = sum(
        weight if model_answers.get(key, default) == value else default
        for key, (value, weight, default) in factors.items()
    )

    magnitude_factor = calculate_magnitude_factor(earthquake_data)
    distance_factor = calculate_distance_factor(
        earthquake_data, user_latitude, user_longitude)

    probability = 0.5 + factors_sum + magnitude_factor + distance_factor
    probability = max(0.0, min(1.0, probability))

    for category, threshold in thresholds.items():
        if probability >= threshold:
            return category, suggested_actions.get(category, "No specific suggestions available")

    return "Unknown", "Unable to determine suggestions at this time."


# def get_earthquake_data_nns(session: Session, user_latitude: float, user_longitude: float):
#     # Query the database for earthquake data including location information
#     earthquakes = (
#         session.query(Earthquake, LocationEarthquake)
#         .join(LocationEarthquake)
#         .all()
#     )

#     if not earthquakes:
#         # Handle case where there are no earthquakes in the database
#         return None

#     # Extract latitude and longitude from the earthquake data
#     earthquake_coordinates = [
#         (location.latitude, location.longitude)
#         for _, location in earthquakes
#     ]

#     # Create a KDTree from the earthquake data
#     kdtree = KDTree(earthquake_coordinates)

#     # Query the KDTree to find the index of the nearest earthquake
#     distance, index = kdtree.query([(user_latitude, user_longitude)], k=1)

#     # Get the earthquake data for the nearest neighbor
#     nearest_earthquake = earthquakes[index[0]][0]

#     return nearest_earthquake


def generate_specific_suggestions(model_answers):
    suggestions = []

    def add_suggestion(condition, text):
        if condition:
            suggestions.append(text)

    add_suggestion(
        model_answers.get("housing_type") == HOUSING_TYPE_APARTMENT,
        SUGGESTION_HOUSING_TYPE
    )

    add_suggestion(
        model_answers.get("emergency_resources"),
        SUGGESTION_EMERGENCY_RESOURCES
    )

    add_suggestion(
        model_answers.get("evacuation_plan"),
        SUGGESTION_EVACUATION_PLAN
    )

    add_suggestion(
        model_answers.get("experience_emergency"),
        SUGGESTION_EXPERIENCE_EMERGENCY
    )

    add_suggestion(
        model_answers.get("medical_conditions"),
        SUGGESTION_MEDICAL_CONDITIONS
    )

    add_suggestion(
        model_answers.get("participation_drills"),
        SUGGESTION_PARTICIPATION_DRILLS
    )

    add_suggestion(
        model_answers.get("communication_device"),
        SUGGESTION_COMMUNICATION_DEVICE
    )

    return suggestions
