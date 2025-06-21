import tkinter as tk
from calculations import normality

def get_frame(parent):
    frame = tk.Frame(parent, bg="white")

    labels = [
        "Equivalent Weight (g/eq)",
        "Mass (g)",
        "Volume (L)",
        "Normality (N)"
    ]

    entries = {}
    for i, label in enumerate(labels):
        tk.Label(frame, text=label, bg="white").grid(row=i, column=0, padx=10, pady=5, sticky="e")
        e = tk.Entry(frame)
        e.grid(row=i, column=1)
        entries[label] = e

    result = tk.StringVar()

    def calculate():
        try:
            mapping = {
                "Equivalent Weight (g/eq)": "eq_weight",
                "Mass (g)": "mass",
                "Volume (L)": "volume",
                "Normality (N)": "normality"
            }

            values = {}
            missing = None
            for label in labels:
                val = entries[label].get().strip()
                if val:
                    values[mapping[label]] = float(val)
                else:
                    if missing:
                        result.set("Leave only one field blank.")
                        return
                    missing = mapping[label]
                    values[mapping[label]] = None

            out = normality.calculate_normality(**values)
            lines = [f"{k.replace('_', ' ').title()}: {round(v, 4)}" for k, v in out.items()]
            result.set("\n".join(lines))
        except Exception as e:
            result.set(f"Error: {e}")

    tk.Button(frame, text="Calculate", command=calculate, bg="#4a90e2", fg="white").grid(row=4, column=0, columnspan=2, pady=10)
    tk.Label(frame, textvariable=result, fg="green", bg="white", justify="left").grid(row=5, column=0, columnspan=2)

    return frame
