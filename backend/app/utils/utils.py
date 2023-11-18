from app.domain.models import Meteorite, Fall, Reclass, MeteoriteGeolocation


def parse_csv_entry(entry):
    cleaned_entry = entry[0].strip('[').strip(']').replace(';;', '')
    return cleaned_entry.split(',')


def create_meteorite_object(cleaned_entry):
    cleaned_entry = [field.strip() if field !=
                     '' else None for field in cleaned_entry]

    return Meteorite(
        name=cleaned_entry[0],
        nametype=cleaned_entry[2],
        mass=float(cleaned_entry[4]) if cleaned_entry[4] else None,
        year=int(cleaned_entry[6]) if cleaned_entry[6] else None,
    )


def create_fall_object(cleaned_entry):
    return Fall(type_name=cleaned_entry[5],)


def create_reclass_object(cleaned_entry):
    return Reclass(name=cleaned_entry[3])


def create_geolocation_object(cleaned_entry):
    return MeteoriteGeolocation(
        reclat=float(cleaned_entry[7]) if cleaned_entry[7] else None,
        reclong=float(cleaned_entry[8]) if cleaned_entry[8] else None)
