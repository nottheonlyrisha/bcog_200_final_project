# BCOG 200 Final Project
## Project Plan
For my final project, I will be creating a rhythm annotation program. After a starting countdown based on the tempo the user selects, the user will click the space bar a number of times, spacing the clicks as long or short as they want to. This program will take these clicks and, using the pre-confirmed tempo, annotate them into readable sheet music (showing just the rhythm/note length of the hits).
### Possible Output Design
![rhythm sheet music - different note lengths on a single line, denotating only the rhythm of the piece](https://github.com/user-attachments/assets/33c0b518-85cc-4853-9aad-edee10100261)

## The Basics
This program can be used to create notation for rhythms that a user taps out. Based on a selected tempo, or speed (which determines the lengths of notes used), the tapped rhythms will be translated into visible sheet music.
## The Code
This program will be contained in a class, like a GUI, and output different Tkinter screens correcponding to and recording user selection and interactions.
**NOTE: please make sure PIL (pillow/Python Image Library) is installed and that you have moved all four images to a folder called "images" _within_ whatever folder the final_project.py is saved in _before_ running this code!!**
### Selection Screen
This screen includes three tempo options as buttons, and a slider to select how many beats are in the countoff (which ranges from 2 to 8 beats).
### Countoff Screen
This is the screen where the chosen number of countoff beats will be displayed at the chosen tempo. The entire screen will flash in time, and the amount of times that the user chooses.
### Rhythm Entry Screen
On this screen, a small box will flash whenever the user taps the space bar. There will also be a submit button, which (as per the prior warning) will omit the last click.
### Loading Screen
This screen might include a progress bar.
### Final Rhythm Screen
This screen will display the final rhythm. If I can find a way to make the final rhythm into a downloadable PNG or other image, there will be a button to download the final sheet music.

### Function Plans
#### Function 1: flash screen
This function will take the tempo selected and change the color of the screen in time with the selected millisecond tempo.
#### Function 2: in-between times recorder
This function will determine how long the spaces between clicks of a key are, preferably in seconds, and record and store the times as individual note lengths.
#### Function 3: time to note converter
This function will be passed the times of each individual note from the previous function, and by comparing the times to the BPM selected, convert the clicks to their corresponding note lengths and store them as such (ex. `note1 = half_note`)
#### and many more!

## Uses
This program could be used to determine notation for a possible song, drumline, or assist in arranging music. It could also be used for fun!
