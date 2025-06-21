import tkinter as tk
from tkinter import ttk

class SplashScreen:
    def __init__(self, root, on_complete):
        self.root = root
        self.on_complete = on_complete

        self.window = tk.Toplevel(root)
        self.window.overrideredirect(True)
        self.window.geometry("500x300+400+200")
        self.window.configure(bg="white")

        tk.Label(self.window, text="H.A.R.I.S.", font=("Segoe UI", 26, "bold"), bg="white", fg="#2c3e50").pack(pady=40)
        tk.Label(self.window, text="Hybrid Analytical Research Integrated Solution", font=("Segoe UI", 10), bg="white", fg="#555").pack()

        self.progress = ttk.Progressbar(self.window, orient="horizontal", length=300, mode="determinate")
        self.progress.pack(pady=30)
        self.progress["maximum"] = 100
        self.progress["value"] = 0

        self.simulate_loading()

    def simulate_loading(self):
        if self.progress["value"] < 100:
            self.progress["value"] += 2
            self.window.after(30, self.simulate_loading)
        else:
            self.window.destroy()
            self.on_complete()