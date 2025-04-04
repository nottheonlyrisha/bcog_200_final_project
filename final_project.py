import tkinter as tk
from tkinter import messagebox #error messages!!

def screen1(): #tempo screen
    main_window = tk.Tk()

    tk.Label(main_window, text="tempo").grid(row=0)
    tempo_entry = tk.Entry(main_window, bg="white")
    tempo_entry.grid(row=1)
    
    def sumbit():
        tempo = tempo_entry.get()
        if tempo == "":
            messagebox.showinfo("error", "please enter a tempo")
        elif int(tempo) <= 59 or int(tempo) >= 241:
            messagebox.showinfo("error", "unsupported tempo: please enter a tempo between 60-240 bpm")
        elif int(tempo)/4 != int(tempo)//4:
            messagebox.showinfo("error", "improper tempo: please enter a tempo divisible by 4")
        else:
            main_window.destroy()
            return tempo
    
    submit_button = tk.Button(main_window, text="submit", command=sumbit)
    submit_button.grid(row=2)

    main_window.mainloop()

def screen2(): #time signature screen
    main_window2 = tk.Tk()

    tk.Label(main_window2, text="time signature:").grid(row=0)
    top_ts_slider = tk.Scale(main_window2, from_=2, to=8, orient=tk.HORIZONTAL, label="top:", activebackground="yellow")
    bottom_ts_slider = tk.Scale(main_window2, from_=2, to=8, orient=tk.HORIZONTAL, label="bottom:", activebackground="yellow")
    top_ts_slider.grid(row=1)
    bottom_ts_slider.grid(row=2)

    def sumbit():
        time_signature = f"{top_ts_slider.get()}/{bottom_ts_slider.get()}"
        if time_signature not in ["2/4", "3/4", "4/4", "6/8"]:
            messagebox.showinfo("error", "unsupported time signature")
        else:
            main_window2.destroy()


    submit_button = tk.Button(main_window2, text="submit", command=sumbit)
    submit_button.grid(row=3)

    main_window2.mainloop()

def screen3(): #countdown select screen
    main_window3 = tk.Tk()

    countdown_slider = tk.Scale(main_window3, from_=2, to=8, orient=tk.HORIZONTAL, label="countoff (beats):", activebackground="yellow")
    countdown_slider.grid(row=0)
     
    def sumbit():
        countoff = countdown_slider.get()
        main_window3.destroy()
        print(countoff)
    
    submit_button = tk.Button(main_window3, text="submit", command=sumbit)
    submit_button.grid(row=1)
    
    main_window3.mainloop()

def main():
    screen1()
    screen2()
    screen3()

if __name__ == "__main__":
    main()