import tkinter as tk

def screen1():
    main_window = tk.Tk()

    tk.Label(main_window, text="tempo").grid(row=0)
    tempo_entry = tk.Entry(main_window, bg="white")
    tempo_entry.grid(row=1)

    def tempo_select():
        tempo = tempo_entry.get()
        main_window.destroy()
        return tempo
    
    submit_button = tk.Button(main_window, text="submit", command=tempo_select)
    submit_button.grid(row=2)

    main_window.mainloop()

def screen2():
    main_window = tk.Tk()

    tk.Label(main_window, text="time signature:").grid(row=0)
    def time_signature_select(i, j):
        time_signature = f"{i}/{j}"
        return time_signature
    time_signatures = ["2/4", "3/4", "4/4", "6/8"]
    time_signature_buttons = []
    for i in range(2,7):
        ts_button = tk.Button(main_window, text=f"{i}/4", command=time_signature_select)
        time_signature_buttons.append(ts_button)

    for i in range(len(time_signature_buttons)):
        for button in time_signature_buttons:
            button.grid(row=i)

    main_window.mainloop()

def main():
    screen1()
    screen2()

if __name__ == "__main__":
    main()