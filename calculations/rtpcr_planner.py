def solve_component(target_conc=None, stock_conc=None, final_vol=None, volume_to_add=None):
    known = {
        "target_conc": target_conc,
        "stock_conc": stock_conc,
        "final_vol": final_vol,
        "volume_to_add": volume_to_add
    }

    missing = [k for k, v in known.items() if v is None]
    if len(missing) == 1:
        m = missing[0]
        if m == "volume_to_add":
            return {"volume_to_add": (target_conc * final_vol) / stock_conc}
        elif m == "target_conc":
            return {"target_conc": (stock_conc * volume_to_add) / final_vol}
        elif m == "stock_conc":
            return {"stock_conc": (target_conc * final_vol) / volume_to_add}
        elif m == "final_vol":
            return {"final_vol": (volume_to_add * stock_conc) / target_conc}
    elif len(missing) == 0:
        return {
            "volume_to_add": (target_conc * final_vol) / stock_conc,
            "target_conc": (stock_conc * volume_to_add) / final_vol,
            "stock_conc": (target_conc * final_vol) / volume_to_add,
            "final_vol": (volume_to_add * stock_conc) / target_conc
        }
    else:
        raise ValueError("Please leave only one field blank or fill all fields to get results.")