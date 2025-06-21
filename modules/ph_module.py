import tkinter as tk
from tkinter import messagebox
import math

def get_frame(parent):
    frame = tk.Frame(parent, bg="white")

    tk.Label(frame, text="pH Calculator", font=("Segoe UI", 14, "bold"), bg="white").pack(pady=10)

    # Mode Selection: Acid or Base
    mode_var = tk.StringVar(value="acid")
    mode_frame = tk.Frame(frame, bg="white")
    tk.Label(mode_frame, text="Type:", bg="white").pack(side="left", padx=(0, 5))
    tk.Radiobutton(mode_frame, text="Acid", variable=mode_var, value="acid", bg="white").pack(side="left")
    tk.Radiobutton(mode_frame, text="Base", variable=mode_var, value="base", bg="white").pack(side="left")
    mode_frame.pack(pady=5)

    # Input: Concentration and Ka/Kb
    conc_frame = tk.Frame(frame, bg="white")
    tk.Label(conc_frame, text="Concentration (mol/L):", width=20, anchor="e", bg="white").pack(side="left")
    conc_entry = tk.Entry(conc_frame)
    conc_entry.pack(side="left")
    conc_frame.pack(pady=5)

    k_frame = tk.Frame(frame, bg="white")
    tk.Label(k_frame, text="Ka or Kb value:", width=20, anchor="e", bg="white").pack(side="left")
    k_entry = tk.Entry(k_frame)
    k_entry.pack(side="left")
    k_frame.pack(pady=5)

    strong_var = tk.IntVar()
    strong_check = tk.Checkbutton(frame, text="Strong Acid/Base", variable=strong_var, bg="white")
    strong_check.pack(pady=5)

    output = tk.StringVar()
    tk.Label(frame, textvariable=output, font=("Segoe UI", 11), fg="green", bg="white").pack(pady=10)

    def calculate_ph():
        try:
            conc = float(conc_entry.get())
            if conc <= 0:
                raise ValueError("Concentration must be positive.")

            if strong_var.get():  # Strong acid/base
                h = conc if mode_var.get() == "acid" else 1e-14 / conc
                ph_value = -math.log10(h)
                output.set(f"{'pH' if mode_var.get() == 'acid' else 'pOH'}: {round(ph_value, 3)}")
                return

            k_val = float(k_entry.get())
            if k_val <= 0:
                raise ValueError("Ka/Kb must be positive.")

            # Weak acid/base: Use sqrt(Ka * C)
            h = math.sqrt(k_val * conc)
            ph = -math.log10(h)

            if mode_var.get() == "acid":
                output.set(f"pH (Weak Acid): {round(ph, 3)}")
            else:
                poh = round(ph, 3)
                ph_value = round(14 - poh, 3)
                output.set(f"pOH: {poh}  →  pH: {ph_value}")

        except Exception as e:
            output.set(f"Error: {e}")

    tk.Button(frame, text="Calculate", command=calculate_ph, bg="#4a90e2", fg="white").pack(pady=5)

    return frame