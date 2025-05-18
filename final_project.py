import tkinter as tk
from tkinter import messagebox #error messages!!
import time
from PIL import Image, ImageTk
import os

class RhythmRecorder(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Rhythm Recorder")
        self.geometry("800x600")
        self.config(bg="white")

        #defaults
        self.tempo = None
        self.time_signature = None
        self.count_off = None
        self.rhythm_data = []

        #startup
        self.setup_screen()
    
    def setup_screen(self):
        for widget in self.winfo_children():
            widget.destroy()           #new screen every time
        tk.Label(self, text="Instructions", font=("Georgia", 16), bg="white").grid(row=0, column=0, columnspan=4)
        instructions = """Select a tempo and an amount of countoff beats. Once you click submit, the screen will flash 
        white at a certain speed - this is the speed of one beat (ie. a "quarter note"). Once the rhythm entry screen 
        appears, tap the spacebar to whatever rhythm you wish, keeping the shortest notes "eighth notes" - half of 
        the space in between flashes - and the longest notes "whole notes" - 4 flashes' worth. Remember to press 
        space after your last note, before you click "Finish" - the last note length will be omitted otherwise."""
        tk.Label(self, text=instructions, font=("Georgia", 12), bg="white").grid(row=1, column=0, columnspan=4)
        tk.Label(self, text="Tempo", font=("Georgia", 16), bg="white").grid(row=2, column=0, sticky="E")

        #tempo select buttons (all in same row)
        self.slow = tk.Button(self, text="Slow", font=("Georgia", 12), command=lambda: self.tempo_select("Slow", self.slow))
        self.slow.grid(row=2, column=1, sticky="W")

        self.moderate = tk.Button(self, text="Moderate", font=("Georgia", 12), command=lambda: self.tempo_select("Moderate", self.moderate))
        self.moderate.grid(row=2, column=1)

        self.fast = tk.Button(self, text="Fast", font=("Georgia", 12), command=lambda: self.tempo_select("Fast", self.fast))
        self.fast.grid(row=2, column=1, sticky="E")

        #countoff slider (all in one row)
        tk.Label(self, text="Count-Off Beats", font=("Georgia", 16), bg="white").grid(row=3, column=0, sticky="E")
        self.count_off_var = tk.IntVar(value=2)
        tk.Scale(self, from_=2, to=8, font=("Georgia", 12), orient="horizontal", bg="white", highlightbackground="white", length=300, variable=self.count_off_var).grid(row=3, column=1)

        #submit button
        tk.Button(self, text="Submit", font=("Georgia", 12), command=self.submit).grid(row=4, column=0, columnspan=4)

    def tempo_select(self, tempo, button):
        self.slow.config(bg="grey94", fg="black", state="normal")
        self.moderate.config(bg="grey94", fg="black", state="normal")
        self.fast.config(bg="grey94", fg="black", state="normal")
        button.config(bg="light sky blue", state="disabled")    #changes color of selected button ONLY
        self.tempo = tempo
        return self.tempo
    
    def submit(self):
        if self.tempo is None:
            messagebox.showinfo("error", "please select a tempo")
        else:
            self.count_off = self.count_off_var.get()
            self.countoff_screen()      #move to next screen
      
    def countoff_screen(self):
        for widget in self.winfo_children():
            widget.destroy()        #"deletes" previous screen - move on with ease

        #flash countoff speed
        self.flash_speed = {"Slow": 1000, "Moderate": 500, "Fast": 250}[self.tempo]
        self.flash_count = self.count_off
        self.flash_screen(self.flash_speed)
    
    def flash_screen(self, speed):
        #flashes selected amount of times at selected speed
        if self.flash_count > 0:
            self.config(bg="SlateBlue2")    #pretty color
            self.after(speed, lambda: self.config(bg="white"))
            self.flash_count -= 1
            self.after(speed * 2, lambda: self.flash_screen(speed))
        else:
            self.rhythm_entry_screen()
    
    def rhythm_entry_screen(self):
        for widget in self.winfo_children():
            widget.destroy()
        
        tk.Label(self, text="Tap spacebar to enter rhythm", font=("Georgia", 12)).pack()

        #flashing box
        self.canvas = tk.Canvas(self, width=200, height=200, bg="white")
        self.canvas.pack()
        self.rect = self.canvas.create_rectangle(50, 50, 150, 150, fill="gray")

        #get taps
        self.bind("<space>", self.record_taps)

        self.start_time = time.time()
        self.rhythm_data = []
        
        #finish button
        tk.Button(self, text="Finish", font=("Georgia", 12), command=self.processing_screen).pack()
    
    def record_taps(self, event):
        self.rhythm_data.append(time.time() - self.start_time)

        #flashes
        self.canvas.itemconfig(self.rect, fill="SlateBlue2")
        self.after(200, lambda: self.canvas.itemconfig(self.rect, fill="gray"))
    
    def processing_screen(self):
        for widget in self.winfo_children():
            widget.destroy()

        #may delete, just so personal computer doesn't explode
        tk.Label(self, text="Processing...", font=("Georgia", 12)).pack()
        self.process_rhythm()
        self.after(2000, self.rhythm_display_screen)

    def process_rhythm(self):
        self.rhythm_data = [self.rhythm_data[i] - self.rhythm_data[i-1] for i in range(1, len(self.rhythm_data))]   #get times in between clicks
        note_lengths = {0.5: "eighth", 1: "quarter", 2: "half", 4: "whole"}     #round times
        modifier = self.flash_speed / 500       #modify to tempo
        #get note sequence
        note_lengths = {key * modifier: value for key, value in note_lengths.items()}
        rounded_rhythm = [min(note_lengths.keys(), key=lambda x: abs(x - time_gap)) for time_gap in self.rhythm_data]
        self.note_sequence = [note_lengths[n] for n in rounded_rhythm]

    def rhythm_display_screen(self):
        for widget in self.winfo_children():
            widget.destroy()

        tk.Label(self, text="Final Rhythm", font=("Georgia", 12), bg="white").pack()
        frame = tk.Frame(self)
        frame.pack()

        #display rhythm (note by note)
        images = {"eighth": "eighth_note_image.png", "quarter": "quarter_note_image.png", "half": "half_note_image.png", "whole": "whole_note_image.png"}
        for note in self.note_sequence:
            path = os.getcwd()
            img = Image.open(os.path.join(f"{path}", "images", images[note]))
            img = img.resize((50, 50))
            tk_image = ImageTk.PhotoImage(img)
            label = tk.Label(frame, image=tk_image)
            label.image = tk_image
            label.pack(side="left")


def main():
    rhythm_recorder = RhythmRecorder()
    rhythm_recorder.mainloop()

if __name__ == "__main__":
    main()