import tkinter as tk

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("H.A.R.I.S.")
        self.root.geometry("1000x700")
        self.root.configure(bg="white")
        self.root.resizable(False, False)

        self.sidebar = tk.Frame(root, bg="#2c3e50", width=200)
        self.sidebar.pack(side="left", fill="y")

        # Brand
        tk.Label(self.sidebar, text="H.A.R.I.S.", font=("Segoe UI", 16, "bold"), bg="#2c3e50", fg="white").pack(pady=(20, 5))
        tk.Label(self.sidebar, text="Hybrid Analytical\nResearch Integrated\nSolution", font=("Segoe UI", 9), justify="center", bg="#2c3e50", fg="#b0bec5").pack()

        # Main content container
        self.container = tk.Frame(root, bg="white")
        self.container.pack(side="right", expand=True, fill="both")

    def add_module(self, label, module):
        tk.Button(self.sidebar, text=label, width=24, anchor="w", font=("Segoe UI", 10),
                  bg="#4a90e2", fg="white", relief="flat",
                  command=lambda m=module: self.show_module(m)).pack(pady=3, padx=10, anchor="w")

    def show_module(self, module):
        for widget in self.container.winfo_children():
            widget.destroy()
        frame = module.get_frame(self.container)
        frame.pack(fill="both", expand=True)