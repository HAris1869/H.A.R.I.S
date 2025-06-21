import tkinter as tk

def get_frame(parent):
    frame = tk.Frame(parent, bg="white")

    tk.Label(frame, text="PCR Mastermix Calculator", font=("Segoe UI", 14, "bold"), bg="white").pack(pady=10)

    reagents = ["Buffer", "dNTPs", "Primers", "Taq", "Template", "Water"]
    entries = {}
    for reagent in reagents:
        tk.Label(frame, text=f"{reagent} per reaction (µL):", bg="white").pack()
        e = tk.Entry(frame)
        e.pack()
        entries[reagent] = e

    tk.Label(frame, text="Number of reactions:", bg="white").pack()
    num_entry = tk.Entry(frame)
    num_entry.pack()

    result = tk.StringVar()

    def calculate():
        try:
            n = int(num_entry.get())
            lines = []
            for reagent in reagents:
                vol = float(entries[reagent].get())
                total = round(vol * n * 1.1, 2)  # 10% overage
                lines.append(f"{reagent}: {total} µL")
            result.set("\n".join(lines))
        except Exception as e:
            result.set(f"Error: {e}")

    tk.Button(frame, text="Calculate", command=calculate, bg="#4a90e2", fg="white").pack(pady=10)
    tk.Label(frame, textvariable=result, bg="white", fg="green", justify="left").pack()

    return frame