def convert_mass(value, from_unit, to_unit):
    scale = {"g": 1, "mg": 1e-3, "µg": 1e-6, "ng": 1e-9}
    return value * (scale[from_unit] / scale[to_unit])

def convert_volume(value, from_unit, to_unit):
    scale = {"L": 1, "mL": 1e-3, "µL": 1e-6, "nL": 1e-9}
    return value * (scale[from_unit] / scale[to_unit])