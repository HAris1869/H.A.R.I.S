import tkinter as tk

def get_frame(parent):
    frame = tk.Frame(parent, bg="white")
    tk.Label(frame, text="Unit Converter", font=("Segoe UI", 14, "bold"), bg="white").pack(pady=10)

    # --- VOLUME CONVERTER ---
    tk.Label(frame, text="Volume Units", font=("Segoe UI", 12, "underline"), bg="white").pack()
    volume_units = [("Liters (L)", 1e0), ("Milliliters (mL)", 1e3), ("Microliters (µL)", 1e6), ("Nanoliters (nL)", 1e9)]
    volume_entries = {}

    for name, _ in volume_units:
        row = tk.Frame(frame, bg="white")
        row.pack(anchor="w", padx=20)
        tk.Label(row, text=name + ":", bg="white", width=18, anchor="e").pack(side="left")
        entry = tk.Entry(row, width=20)
        entry.pack(side="left")
        volume_entries[name] = entry

    def convert_volume():
        filled = [(name, float(e.get())) for name, e in volume_entries.items() if e.get()]
        if len(filled) != 1:
            volume_status.set("Fill only one volume field.")
            return
        name, value = filled[0]
        base = next(f for n, f in volume_units if n == name)
        L = value / base
        for n, factor in volume_units:
            volume_entries[n].delete(0, tk.END)
            volume_entries[n].insert(0, round(L * factor, 8))
        volume_status.set("Volume conversion successful.")

    volume_status = tk.StringVar()
    tk.Button(frame, text="Convert Volume", command=convert_volume, bg="#4a90e2", fg="white").pack(pady=5)
    tk.Label(frame, textvariable=volume_status, bg="white", fg="green").pack()

    # --- MASS CONVERTER ---
    tk.Label(frame, text="Mass Units", font=("Segoe UI", 12, "underline"), bg="white").pack(pady=(20,0))
    mass_units = [("Grams (g)", 1e0), ("Milligrams (mg)", 1e3), ("Micrograms (µg)", 1e6), ("Nanograms (ng)", 1e9)]
    mass_entries = {}

    for name, _ in mass_units:
        row = tk.Frame(frame, bg="white")
        row.pack(anchor="w", padx=20)
        tk.Label(row, text=name + ":", bg="white", width=18, anchor="e").pack(side="left")
        entry = tk.Entry(row, width=20)
        entry.pack(side="left")
        mass_entries[name] = entry

    def convert_mass():
        filled = [(name, float(e.get())) for name, e in mass_entries.items() if e.get()]
        if len(filled) != 1:
            mass_status.set("Fill only one mass field.")
            return
        name, value = filled[0]
        base = next(f for n, f in mass_units if n == name)
        g = value / base
        for n, factor in mass_units:
            mass_entries[n].delete(0, tk.END)
            mass_entries[n].insert(0, round(g * factor, 8))
        mass_status.set("Mass conversion successful.")

    mass_status = tk.StringVar()
    tk.Button(frame, text="Convert Mass", command=convert_mass, bg="#4a90e2", fg="white").pack(pady=5)
    tk.Label(frame, textvariable=mass_status, bg="white", fg="green").pack()

    return frame