# Standard Library Imports
from fastapi import HTTPException
# Third-Party Imports
from sqlalchemy.orm import Session
from sqlalchemy import func

# Local Imports
from app.domain.models import Earthquake, LocationEarthquake, Magnitude
from app.core.thresholds import thresholds, suggested_actions, magnitude_thresholds
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


def get_earthquake_data(db: Session, user_latitude: float, user_longitude: float, radius: float = 500000):
    """
    Returns a list of earthquake data within a given radius of the user's location.
    Parameters:
        db (Session): Database session
        user_latitude (float): User's latitude
        user_longitude (float): User's longitude
        radius (float): Radius in meters (500km)
    returns:
        List of earthquake data within a given radius of the user's location
    """
    try:
        # Create the user point using the SQLalchemy func library
        user_point = func.ST_GeomFromText(
            f'POINT({user_longitude} {user_latitude})', 4326)

        nearest_earthquake = (
            db.query(Earthquake)
            .join(LocationEarthquake, Earthquake.id == LocationEarthquake.earthquake_id)
            .join(Magnitude, Earthquake.id == Magnitude.earthquake_id)
            .filter(func.ST_DistanceSphere(LocationEarthquake.geom, user_point) <= radius)
            .order_by(Magnitude.mag.desc())
            .limit(100)
            .all()
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    return nearest_earthquake


def calculate_average_magnitude(earthquake_data):
    """
    Calculates the average magnitude from a list of earthquake data.
    Parameters:
        earthquake_data (List[Earthquake]): List of earthquake data
    Returns:
        float: Average magnitude
    """

    # Extract magnitudes from earthquake data, filtering out None values
    magnitudes = [
        magnitude.mag for earthquake in earthquake_data if earthquake.magnitude is not None for magnitude in earthquake.magnitude
    ]

    if magnitudes:
        average_magnitude = sum(magnitudes) / 100

        # Find the category based on the average magnitude
        for category, threshold in magnitude_thresholds.items():
            if average_magnitude >= threshold:
                return category, average_magnitude
    else:
        return 0.0


def calculate_probability(model_answers):
    """
    Calculate the probability of an earthquake based on model answers and average magnitude.
    Parameters:
        model_answers (FormBase): User's answers to the form
        average_magnitude (float): Average magnitude of earthquakes in the area
    Returns:
        Probability of an earthquake occurring
    """

    # Extract relevant information from model answers
    housing_factor = 0.1 if model_answers.housing_type == "Apartment" else 0.0
    emergency_resources_factor = 0.0 if model_answers.emergency_resources else 0.2
    evacuation_plan_factor = 0.0 if model_answers.evacuation_plan else 0.2
    experience_emergency_factor = 0.0 if model_answers.experience_emergency else 0.1
    medical_conditions_factor = 0.0 if model_answers.medical_conditions else 0.1
    participation_drills_factor = 0.0 if model_answers.participation_drills else 0.1
    comunication_device_factor = 0.0 if model_answers.comunication_device else 0.1

    # Combine factors to get the final probability
    probability = housing_factor + \
        emergency_resources_factor + evacuation_plan_factor + \
        experience_emergency_factor + medical_conditions_factor + \
        participation_drills_factor + comunication_device_factor

    # Ensure probability is within the valid range [0, 1]
    probability = max(0.0, min(1.0, probability))

    for category, threshold in thresholds.items():
        if probability >= threshold:
            return category, suggested_actions.get(category, "No specific suggestions available")

    return "Unknown", "Unable to determine suggestions at this time."


def generate_specific_suggestions(model_answers):
    suggestions = []

    if model_answers.housing_type == HOUSING_TYPE_APARTMENT:
        suggestions.append(SUGGESTION_HOUSING_TYPE)
    if not model_answers.emergency_resources:
        suggestions.append(SUGGESTION_EMERGENCY_RESOURCES)
    if not model_answers.evacuation_plan:
        suggestions.append(SUGGESTION_EVACUATION_PLAN)
    if not model_answers.experience_emergency:
        suggestions.append(SUGGESTION_EXPERIENCE_EMERGENCY)
    if not model_answers.medical_conditions:
        suggestions.append(SUGGESTION_MEDICAL_CONDITIONS)
    if not model_answers.participation_drills:
        suggestions.append(SUGGESTION_PARTICIPATION_DRILLS)
    if not model_answers.comunication_device:
        suggestions.append(SUGGESTION_COMMUNICATION_DEVICE)

    return suggestions
