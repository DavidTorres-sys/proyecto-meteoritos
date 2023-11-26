thresholds = {
    "Very Low": 0.8,
    "Low": 0.6,
    "Medium": 0.4,
    "High": 0.2,
    "Very High": 0.0,
}

magnitude_thresholds = {
    "Very High": 7.0,
    "High": 6.0,
    "Medium": 4.0,
    "Low": 3.0,
    "Very Low": 0.0,
}

suggested_actions = {
    "Very High": "Consider reinforcing your living space and having emergency supplies readily available.",
    "High": "Ensure you have an evacuation plan in place and regularly participate in emergency drills.",
    "Medium": "Stay informed about emergency procedures and have basic emergency supplies.",
    "Low": "Familiarize yourself with evacuation routes and have a basic emergency kit.",
    "Very Low": "Stay informed about local emergency procedures and have basic emergency supplies.",
}

factors = {
    "housing_type": ("Apartment", 0.1, 0.5),
    "emergency_resources": (True, 0.2, 0.3),
    "evacuation_plan": (True, 0.1, 0.4),
    "experience_emergency": (True, 0.1, 0.0),
    "medical_conditions": (True, 0.1, 0.0),
    "participation_drills": (True, 0.1, 0.0),
    "comunication_device": (True, 0.1, 0.0)
}
