import tkinter as tk
from tkinter import messagebox #error messages!!
import time

class RhythmRecorder:
    def __init__(self, root):
        self.root = root
        self.root.title("Rhythm Recorder")

        self.setup_screen()
    
    def setup_screen(self):
        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack(padx=10, pady=10)

        #buttons frame
        self.buttons_frame = tk.Frame(self.main_frame)
        self.buttons_frame.pack()

        #sliders frame
        self.sliders_frame = tk.Frame(self.main_frame)
        self.sliders_frame.pack()

        #submit button frame
        self.submit_frame = tk.Frame(self.main_frame)
        self.submit_frame.pack()

        #tempo selection
        tempo_label = tk.Label(self.buttons_frame, text="tempo")
        tempo_label.pack()
        
        self.slow = tk.Button(self.buttons_frame, text="slow", command=lambda: self.tempo_select("slow", self.slow))
        self.moderate = tk.Button(self.buttons_frame, text="moderate", command=lambda: self.tempo_select("moderate", self.moderate))
        self.fast = tk.Button(self.buttons_frame, text="fast", command=lambda: self.tempo_select("fast", self.fast))
        self.slow.pack(side="left")
        self.moderate.pack(side="left")
        self.fast.pack(side="left")

        #tempo

        #time signature selection
        self.top_ts_slider = tk.Scale(self.sliders_frame, from_=2, to=8, orient=tk.HORIZONTAL, label="top:", activebackground="yellow")
        self.bottom_ts_slider = tk.Scale(self.sliders_frame, from_=2, to=8, orient=tk.HORIZONTAL, label="bottom:", activebackground="yellow")
        self.top_ts_slider.pack()
        self.bottom_ts_slider.pack()

        #countoff selection
        self.countdown_slider = tk.Scale(self.sliders_frame, from_=2, to=8, orient=tk.HORIZONTAL, label="countoff (beats):", activebackground="yellow")
        self.countdown_slider.pack()

        #submit button
        self.submit = tk.Button(self.submit_frame, text="submit", command=self.submit)
        self.submit.pack()

    def tempo_select(self, tempo, button):
        self.slow.config(bg="grey94", state="normal")
        self.moderate.config(bg="grey94", state="normal")
        self.fast.config(bg="grey94", state="normal")
        button.config(bg="yellow", state="disabled")
        print(tempo)
        return tempo
    
    def submit(self):
        ts = f"{self.top_ts_slider.get()}/{self.bottom_ts_slider.get()}"
        print(ts)
      

def screen1(): #tempo screen
    main_window = tk.Tk()

    tk.Label(main_window, text="tempo").grid(row=0)
    tempo_entry = tk.Entry(main_window, bg="white")
    tempo_entry.grid(row=1)
    
    def submit():
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
    
    submit_button = tk.Button(main_window, text="submit", command=submit)
    submit_button.grid(row=2)

    main_window.mainloop()

def screen2(): #time signature screen
    main_window2 = tk.Tk()

    tk.Label(main_window2, text="time signature:").grid(row=0)
    top_ts_slider = tk.Scale(main_window2, from_=2, to=8, orient=tk.HORIZONTAL, label="top:", activebackground="yellow")
    bottom_ts_slider = tk.Scale(main_window2, from_=2, to=8, orient=tk.HORIZONTAL, label="bottom:", activebackground="yellow")
    top_ts_slider.grid(row=1)
    bottom_ts_slider.grid(row=2)

    def submit():
        time_signature = f"{top_ts_slider.get()}/{bottom_ts_slider.get()}"
        if time_signature not in ["2/4", "3/4", "4/4", "6/8"]:
            messagebox.showinfo("error", "unsupported time signature")
        else:
            main_window2.destroy()
            return time_signature

    submit_button = tk.Button(main_window2, text="submit", command=submit)
    submit_button.grid(row=3)

    main_window2.mainloop()

def screen3(): #countdown select screen
    main_window3 = tk.Tk()

    countdown_slider = tk.Scale(main_window3, from_=2, to=8, orient=tk.HORIZONTAL, label="countoff (beats):", activebackground="yellow")
    countdown_slider.grid(row=0)
     
    def submit():
        countoff = countdown_slider.get()
        main_window3.destroy()
        return countoff

    submit_button = tk.Button(main_window3, text="submit", command=submit)
    submit_button.grid(row=1)

    main_window3.mainloop()

def screen4(tempo, time_signature, countoff):
    tempo = 60 / tempo #number of seconds in a beat/between notes


def main():
    root = tk.Tk()
    rhythm_recorder = RhythmRecorder(root=root)
    rhythm_recorder.root.mainloop()

    # screen1()
    # screen2()
    # screen3()

if __name__ == "__main__":
    main()