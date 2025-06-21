def percent_solution_wv(mass=None, volume=None, percent=None):
    missing = [v is None for v in [mass, volume, percent]].count(True)

    if missing > 1:
        raise ValueError("Leave only one field blank.")
    elif missing == 1:
        if percent is None:
            return {"percent": (mass / volume) * 100}
        elif mass is None:
            return {"mass": (percent / 100) * volume}
        elif volume is None:
            return {"volume": mass / (percent / 100)}
    elif missing == 0:
        # All provided: validate
        expected_percent = (mass / volume) * 100
        return {
            "percent": round(expected_percent, 4),
            "mass": round(mass, 4),
            "volume": round(volume, 4)
        }
    else:
        raise ValueError("Invalid input.")