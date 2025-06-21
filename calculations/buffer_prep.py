def calculate_buffer_volume(desired_conc=None, stock_conc=None, final_volume=None, volume_needed=None):
    missing = [v is None for v in [desired_conc, stock_conc, final_volume, volume_needed]].count(True)

    if missing > 1:
        raise ValueError("Leave only one field blank.")
    elif missing == 1:
        if volume_needed is None:
            return {"volume_needed": (desired_conc * final_volume) / stock_conc}
        elif desired_conc is None:
            return {"desired_conc": (stock_conc * volume_needed) / final_volume}
        elif stock_conc is None:
            return {"stock_conc": (desired_conc * final_volume) / volume_needed}
        elif final_volume is None:
            return {"final_volume": (stock_conc * volume_needed) / desired_conc}
    elif missing == 0:
        volume_needed = (desired_conc * final_volume) / stock_conc
        return {
            "desired_conc": round(desired_conc, 4),
            "stock_conc": round(stock_conc, 4),
            "final_volume": round(final_volume, 4),
            "volume_needed": round(volume_needed, 4)
        }
    else:
        raise ValueError("Invalid input.")