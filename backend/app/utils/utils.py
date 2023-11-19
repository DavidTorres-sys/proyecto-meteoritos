from app.domain.models import Earthquake, Location, Magnitude, Source, Status


def parse_csv_entry(entry):
    cleaned_entry = entry[0].strip(
        '[').strip(']').replace(';;;;;;;;;;;;;;;;', '')
    return cleaned_entry.split(',')


def create_earthquake_object(cleaned_entry):
    return Earthquake(
        time=cleaned_entry[0] if cleaned_entry[0] else None,
        updated=cleaned_entry[12] if cleaned_entry[12] else None,
    )


def create_location_object(cleaned_entry):
    return Location(
        latitude=cleaned_entry[1] if cleaned_entry[1] else None,
        longitude=cleaned_entry[2] if cleaned_entry[2] else None,
    )


def create_magnitude_object(cleaned_entry):
    horizontal_error = cleaned_entry[15] if cleaned_entry[15] else None

    # Verifica y corrige el tipo de dato para "horizontalError"
    if horizontal_error is not None:
        try:
            horizontal_error = float(horizontal_error)
        except ValueError:
            # Manejo de error si no se puede convertir a float
            horizontal_error = None

    return Magnitude(
        mag=cleaned_entry[4] if cleaned_entry[4] else None,
        magType=cleaned_entry[5] if cleaned_entry[5] else None,
        nst=cleaned_entry[6] if cleaned_entry[6] else None,
        gap=cleaned_entry[7] if cleaned_entry[7] else None,
        dmin=cleaned_entry[8] if cleaned_entry[8] else None,
        rms=cleaned_entry[9] if cleaned_entry[9] else None,
        horizontalError=horizontal_error,
        depthError=cleaned_entry[16] if cleaned_entry[16] else None,
        magError=cleaned_entry[17] if cleaned_entry[17] else None,
        magNst=cleaned_entry[18] if cleaned_entry[18] else None,
    )


def create_source_object(cleaned_entry):
    return Source(
        net=cleaned_entry[10] if cleaned_entry[10] else None,
        locationSource=cleaned_entry[20] if cleaned_entry[20] else None,
        magSource=cleaned_entry[21] if cleaned_entry[21] else None,
    )


def create_status_object(cleaned_entry):
    return Status(
        status=cleaned_entry[19] if cleaned_entry[19] else None,
    )
