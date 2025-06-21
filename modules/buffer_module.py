import tkinter as tk
from calculations import buffer_prep

def get_frame(parent):
    frame = tk.Frame(parent, bg="white")

    labels = [
        "Desired Concentration (M)",
        "Stock Concentration (M)",
        "Final Volume (mL)",
        "Volume Needed (mL)"
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
                "Desired Concentration (M)": "desired_conc",
                "Stock Concentration (M)": "stock_conc",
                "Final Volume (mL)": "final_volume",
                "Volume Needed (mL)": "volume_needed"
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

            out = buffer_prep.calculate_buffer_volume(**values)
            lines = [f"{k.replace('_',' ').title()}: {round(v, 4)}" for k, v in out.items()]
            result.set("\n".join(lines))
        except Exception as e:
            result.set(f"Error: {e}")

    tk.Button(frame, text="Calculate", command=calculate, bg="#4a90e2", fg="white").grid(row=4, columnspan=2, pady=10)
    tk.Label(frame, textvariable=result, fg="green", bg="white", justify="left").grid(row=5, columnspan=2)

    return frame