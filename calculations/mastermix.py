def compute_mastermix(num_rxns, total_per_rxn, components_per_rxn):
    filled = {k: v for k, v in components_per_rxn.items() if v is not None}
    missing = [k for k, v in components_per_rxn.items() if v is None]

    if len(missing) > 1:
        raise ValueError("Please leave only one component blank.")
    elif len(missing) == 1:
        missing_key = missing[0]
        known_sum = sum(filled.values())
        missing_val = total_per_rxn - known_sum
        if missing_val < 0:
            raise ValueError("Sum of components exceeds total per reaction.")
        filled[missing_key] = missing_val
    else:
        total_sum = sum(filled.values())
        if abs(total_sum - total_per_rxn) > 0.01:
            raise ValueError("Sum of all components doesn't match per-reaction volume.")
        missing_key = None

    result = {k: round(v * num_rxns, 2) for k, v in filled.items()}
    result["Total Volume"] = round(total_per_rxn * num_rxns, 2)
    result["Missing Component"] = missing_key or "None (all filled correctly)"
    return result