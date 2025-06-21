def calculate_normality(eq_weight=None, mass=None, volume=None, normality=None):
    missing = [v is None for v in [normality, eq_weight, mass, volume]].count(True)

    if missing > 1:
        raise ValueError("Leave only one field blank.")
    elif missing == 1:
        if normality is None:
            return {"normality": mass / (eq_weight * volume)}
        elif mass is None:
            return {"mass": normality * eq_weight * volume}
        elif eq_weight is None:
            return {"eq_weight": mass / (normality * volume)}
        elif volume is None:
            return {"volume": mass / (eq_weight * normality)}
    elif missing == 0:
        expected_N = mass / (eq_weight * volume)
        return {
            "normality": round(expected_N, 4),
            "mass": round(mass, 4),
            "eq_weight": round(eq_weight, 4),
            "volume": round(volume, 4)
        }
    else:
        raise ValueError("Invalid input.")