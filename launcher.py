import tkinter as tk
from app.splash import SplashScreen
from app.main import App
from modules import (
    qpcr_module, rtpcr_module, buffer_module, molarity_module,
    percent_module, unit_module, normality_module, manualpcr_module,
    mastermix_module, ph_module
)

def launch_main():
    app = App(root)

    tools = {
        "qPCR Planner": qpcr_module,
        "RT-PCR Planner": rtpcr_module,
        "Buffer Calculator": buffer_module,
        "Molarity Calculator": molarity_module,
        "Percent Calculator": percent_module,
        "Unit Converter": unit_module,
        "Normality Calculator": normality_module,
        "Manual PCR Planner": manualpcr_module,
        "MasterMix Planner": mastermix_module,
        "pH Calculator": ph_module
    }

    for label, module in tools.items():
        app.add_module(label, module)

    root.deiconify()

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()
    SplashScreen(root, launch_main)
    root.mainloop()
