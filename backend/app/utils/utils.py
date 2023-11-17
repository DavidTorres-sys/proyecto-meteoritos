from app.domain.models import Meteorite

def parse_csv_entry(entry):
    cleaned_entry = entry[0].strip('[').strip(']').replace(';;', '')
    return cleaned_entry.split(',')

def create_meteorite_object(cleaned_entry):
    geolocation = cleaned_entry[-1].strip('"')
    cleaned_entry = [field.strip() if field != '' else None for field in cleaned_entry]

    return Meteorite(
        name=cleaned_entry[0],
        idMeteorite=int(cleaned_entry[1]) if cleaned_entry[1] else None,
        nametype=cleaned_entry[2],
        recclass=cleaned_entry[3],
        mass=float(cleaned_entry[4]) if cleaned_entry[4] else None,
        fall=cleaned_entry[5],
        year=int(cleaned_entry[6]) if cleaned_entry[6] else None,
        reclat=float(cleaned_entry[7]) if cleaned_entry[7] else None,
        reclong=float(cleaned_entry[8]) if cleaned_entry[8] else None,
        geolocation=geolocation,
    )
