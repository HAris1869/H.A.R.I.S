import tkinter as tk
import time
import threading

def get_frame(parent):
    frame = tk.Frame(parent, bg="white")

    tk.Label(frame, text="Manual PCR Timer", font=("Segoe UI", 14, "bold"), bg="white").pack(pady=10)

    steps = []

    def add_step():
        temp = temp_entry.get()
        duration = time_entry.get()
        if temp and duration:
            steps.append((temp, int(duration)))
            step_list.insert(tk.END, f"{temp}°C for {duration} sec")
            temp_entry.delete(0, tk.END)
            time_entry.delete(0, tk.END)

    def run_steps():
        def countdown():
            for temp, sec in steps:
                status.set(f"{temp}°C — {sec} sec")
                for i in range(sec, 0, -1):
                    timer.set(f"{i} sec")
                    time.sleep(1)
            status.set("PCR Complete")
            timer.set("")

        threading.Thread(target=countdown).start()

    tk.Label(frame, text="Temp (°C):", bg="white").pack()
    temp_entry = tk.Entry(frame)
    temp_entry.pack()

    tk.Label(frame, text="Time (sec):", bg="white").pack()
    time_entry = tk.Entry(frame)
    time_entry.pack()

    tk.Button(frame, text="Add Step", command=add_step, bg="#4a90e2", fg="white").pack(pady=5)

    step_list = tk.Listbox(frame, width=40)
    step_list.pack(pady=5)

    tk.Button(frame, text="Start PCR", command=run_steps, bg="green", fg="white").pack(pady=10)

    status = tk.StringVar()
    timer = tk.StringVar()
    tk.Label(frame, textvariable=status, font=("Segoe UI", 12), bg="white", fg="blue").pack()
    tk.Label(frame, textvariable=timer, font=("Segoe UI", 12), bg="white", fg="red").pack()

    return frame