# BCOG 200 Final Project
## Project Plan
For my final project, I will be creating a rhythm annotation program. After a starting countdown based on the BPM (beats per minute) the user inputs, the user will click a key, probably the space bar, a number of times, spacing the clicks as long or short as they want to. This program will take these clicks and, using the pre-confirmed tempo, annotate them into readable sheet music (showing just the rhythm/note length of the hits). I may also add a feature so users can edit this sheet music by inputting the notes they want after creating the rhythm, which will again change the sheet music to reflect these changes in the key/clef the user chooses.
### Possible Output Designs
![rhythm sheet music - different note lengths on a single line, denotating only the rhythm of the piece](https://github.com/user-attachments/assets/33c0b518-85cc-4853-9aad-edee10100261)

![sheet music for a melody - notes of different lengths and locations on a five-line staff, denotating both the rhythm and tonal notes of the piece](https://github.com/user-attachments/assets/6a1f1cef-0758-432c-91fd-ac71b59fb3db)

_(the latter with or without the letters on top of each note)_
## Function Plans
### Function 1: tempo selection
This function will (probably using the `time` module) allow the user to enter a tempo in BPM (beats per minute), and based on that will set a reference tempo to determine the rhythm's notes (ie. a whole note at 120 BPM is the same as a half note at 60 BPM - this function will tell the program which to use). This function may also be a counter (with up/down arrows), to avoid any BPMs not divisible by 4, a musical convention.
### Function 2: in-between times recorder
This function will determine how long the spaces between clicks of a key are, preferably in seconds, and record and store the times as individual note lengths.
### Function 3: time to note converter
This function will be passed the times of each individual note from the previous function, and by comparing the times to the BPM selected, convert the clicks to their corresponding note lengths and store them as such (ex. `note1 = half_note`)
