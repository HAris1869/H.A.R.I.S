def calculate_molarity_from_mass(mass, volume, mw):
    return mass / (volume * mw)

def calculate_mass_from_molarity(molarity, volume, mw):
    return molarity * volume * mw

def calculate_volume_from_mass(mass, molarity, mw):
    return mass / (molarity * mw)

def calculate_mw_from_mass(mass, molarity, volume):
    return mass / (molarity * volume)