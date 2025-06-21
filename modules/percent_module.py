import tkinter as tk

def get_frame(parent):
    frame = tk.Frame(parent, bg="white")

    tk.Label(frame, text="Percent Solution Calculator", font=("Segoe UI", 14, "bold"), bg="white").pack(pady=10)

    labels = ["Mass (g)", "Volume (mL)", "Percent (%)"]
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
            volume = entries["Volume (mL)"].get()
            percent = entries["Percent (%)"].get()

            values = {
                "mass": float(mass) if mass else None,
                "volume": float(volume) if volume else None,
                "percent": float(percent) if percent else None
            }

            missing = [k for k, v in values.items() if v is None]
            if len(missing) != 1:
                result.set("Leave exactly one field blank.")
                return

            if "percent" in missing:
                values["percent"] = (values["mass"] / values["volume"]) * 100
            elif "mass" in missing:
                values["mass"] = (values["percent"] * values["volume"]) / 100
            elif "volume" in missing:
                values["volume"] = (values["mass"] / values["percent"]) * 100

            output = [f"{k}: {round(v, 4)}" for k, v in values.items()]
            result.set("\n".join(output))
        except Exception as e:
            result.set(f"Error: {e}")

    tk.Button(frame, text="Calculate", command=calculate, bg="#4a90e2", fg="white").pack(pady=10)
    tk.Label(frame, textvariable=result, bg="white", fg="green").pack()

    return frame