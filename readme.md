# BCOG 200 Final Project
## Project Plan
For my final project, I will be creating a rhythm annotation program. After a starting countdown based on the tempo the user selects, the user will click the space bar a number of times, spacing the clicks as long or short as they want to. This program will take these clicks and, using the pre-confirmed tempo, annotate them into readable sheet music (showing just the rhythm/note length of the hits).
### Possible Output Designs
![rhythm sheet music - different note lengths on a single line, denotating only the rhythm of the piece](https://github.com/user-attachments/assets/33c0b518-85cc-4853-9aad-edee10100261)

## Function Plans
### Function 1: flash screen
This function will take the tempo selected and change the color of the screen in time with the selected millisecond tempo.
### Function 2: in-between times recorder
This function will determine how long the spaces between clicks of a key are, preferably in seconds, and record and store the times as individual note lengths.
### Function 3: time to note converter
This function will be passed the times of each individual note from the previous function, and by comparing the times to the BPM selected, convert the clicks to their corresponding note lengths and store them as such (ex. `note1 = half_note`)
### and many more!