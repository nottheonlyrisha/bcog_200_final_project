import tkinter as tk

def screen1(): #tempo screen
    main_window = tk.Tk()

    tk.Label(main_window, text="tempo").grid(row=0)
    tempo_entry = tk.Entry(main_window, bg="white")
    tempo_entry.grid(row=1)
    
    def sumbit():
        tempo = tempo_entry.get()
        main_window.destroy()
        return tempo
    
    submit_button = tk.Button(main_window, text="submit", command=sumbit)
    submit_button.grid(row=2)

    main_window.mainloop()

def screen2(): #time signature screen
    main_window2 = tk.Tk()

    tk.Label(main_window2, text="time signature:").grid(row=0)
    def time_signature_select(ts):
        main_window2.destroy()
        return ts
    
    time_signatures = ["2/4", "3/4", "4/4", "6/8"]
    time_signature_buttons = []
    for ts in time_signatures:
        ts_button = tk.Button(main_window2, text=ts, command=lambda ts=ts: time_signature_select(ts))
        time_signature_buttons.append(ts_button)

    i = 0
    for button in time_signature_buttons:
        button.grid(row=1, column=i)
        i += 1

    main_window2.mainloop()

def screen3(): #countdown select screen
    main_window3 = tk.Tk()

    tk.Label(main_window3, text="countoff (beats):").grid(row=0)

    main_window3.mainloop()

def main():
    screen1()
    screen2()
    screen3()

if __name__ == "__main__":
    main()