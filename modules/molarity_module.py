import tkinter as tk

def get_frame(parent):
    frame = tk.Frame(parent, bg="white")

    tk.Label(frame, text="Molarity Calculator", font=("Segoe UI", 14, "bold"), bg="white").pack(pady=10)

    labels = ["Mass (g)", "Molecular Weight (g/mol)", "Volume (L)", "Molarity (mol/L)"]
    entries = {}
    for label in labels:
        tk.Label(frame, text=label, bg="white").pack()
        e = tk.Entry(frame)
        e.pack()
        entries[label] = e

    result = tk.StringVar()

    def calculate():
        try:
            mass = entries["Mass (g)"].get()
            mw = entries["Molecular Weight (g/mol)"].get()
            vol = entries["Volume (L)"].get()
            molarity = entries["Molarity (mol/L)"].get()

            values = {
                "mass": float(mass) if mass else None,
                "mw": float(mw) if mw else None,
                "vol": float(vol) if vol else None,
                "molarity": float(molarity) if molarity else None
            }

            missing = [k for k, v in values.items() if v is None]
            if len(missing) != 1:
                result.set("Leave exactly one field blank.")
                return

            if "molarity" in missing:
                values["molarity"] = values["mass"] / (values["mw"] * values["vol"])
            elif "mass" in missing:
                values["mass"] = values["molarity"] * values["mw"] * values["vol"]
            elif "mw" in missing:
                values["mw"] = values["mass"] / (values["molarity"] * values["vol"])
            elif "vol" in missing:
                values["vol"] = values["mass"] / (values["molarity"] * values["mw"])

            lines = [f"{k.title()}: {round(v, 4)}" for k, v in values.items()]
            result.set("\n".join(lines))
        except Exception as e:
            result.set(f"Error: {e}")

    tk.Button(frame, text="Calculate", command=calculate, bg="#4a90e2", fg="white").pack(pady=10)
    tk.Label(frame, textvariable=result, bg="white", fg="green", justify="left").pack()

    return frame