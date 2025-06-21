def solve_manual_pcr(total_time=None, cycles=None, denat=None, anneal=None, extend=None):
    # Convert minutes to seconds
    if total_time is not None:
        total_time_sec = total_time * 60
    else:
        total_time_sec = None

    known = {
        "total_time": total_time_sec,
        "cycles": cycles,
        "denat": denat,
        "anneal": anneal,
        "extend": extend
    }

    missing = [k for k, v in known.items() if v is None]

    # Solve for one missing field
    if len(missing) == 1:
        m = missing[0]
        if m == "total_time":
            return {"total_time": (cycles * (denat + anneal + extend)) / 60}
        elif m == "cycles":
            return {"cycles": total_time_sec / (denat + anneal + extend)}
        elif m == "denat":
            return {"denat": total_time_sec / cycles - (anneal + extend)}
        elif m == "anneal":
            return {"anneal": total_time_sec / cycles - (denat + extend)}
        elif m == "extend":
            return {"extend": total_time_sec / cycles - (denat + anneal)}
        else:
            raise ValueError("Unknown field.")

    # All fields filled: provide diagnostic breakdown
    elif len(missing) == 0:
        per_cycle = denat + anneal + extend
        total = cycles * per_cycle
        return {
            "Per Cycle Time (s)": per_cycle,
            "Total Time (min)": total / 60,
            "Total Time (hh:mm:ss)": f"{int(total // 3600):02}:{int((total % 3600) // 60):02}:{int(total % 60):02}"
        }

    else:
        raise ValueError("Please leave exactly one field blank or fill all for summary.")