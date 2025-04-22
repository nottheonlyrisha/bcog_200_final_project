import tkinter as tk
from tkinter import messagebox #error messages!!
import time

class RhythmRecorder:
    def __init__(self, root):
        self.root = root
        self.root.title("Rhythm Recorder")

        self.tempo = None
        self.setup_info = None

        self.setup_screen()
        self.countoff_screen()
    
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
        self.top_ts_slider = tk.Scale(self.sliders_frame, from_=2, to=4, orient=tk.HORIZONTAL, label="top:", activebackground="yellow")
        self.bottom_ts_slider = tk.Scale(self.sliders_frame, from_=4, to=8, orient=tk.HORIZONTAL, label="bottom:", activebackground="yellow")
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
        self.tempo = tempo
        return self.tempo
    
    def submit(self):
        ts = f"{self.top_ts_slider.get()}/{self.bottom_ts_slider.get()}"
        countoff = f"{self.countdown_slider.get()}"
        valid_ts = ["2/4", "3/4", "4/4", "6/8"]
        if ts not in valid_ts:
            messagebox.showinfo("error", "invalid time signature - please enter a standard time signature")
        if self.tempo is None:
            messagebox.showinfo("error", "please select a tempo")
        self.setup_info = self.tempo, ts, countoff
        print(self.setup_info)
        return self.setup_info
      
    def countoff_screen(self):
        self.flash_frame = tk.Frame(self.root)
        self.flash_frame.pack(padx=10, pady=10)

        self.flash = self.root.configure(bg='darkgrey')
        self.regular = self.root.configure(bg='white')

        self.flash

def main():
    root = tk.Tk()
    rhythm_recorder = RhythmRecorder(root=root)
    rhythm_recorder.root.mainloop()


if __name__ == "__main__":
    main()