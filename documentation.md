# BCOG 200 Final Project Documentation
## The Basics
This program can be used to create notation for rhythms that a user taps out. Based on a selected tempo, or speed, and time signature (which determines the types of notes used), the tapped rhythms will be translated into visible sheet music.
## The Code
This program will be contained in a class, like a GUI, and output different Tkinter screens correcponding to and recording user selection and interactions.
### Selection Screen
This screen includes three tempo options as buttons, and three sliders - two to select a time signature (top and bottom numbers), and one to select how many beats are in the countoff (which ranges from 2 to 8 beats). This screen also uses error messages to correct users when they input an unsupported time signature (currently I plan to code for 2/4, 3/4, 4/4, and 6/8).
### Countoff Screen
This is the screen where the chosen number of countoff beats will be displayed at the chosen tempo. This will either include the entire screen flashing in time, or a smaller shape flashing. I may also include multiple dots that are centered on the screen, that appear on beat one at a time (this may not happen).
### Rhythm Entry Screen
This screen will either flash as a whole or a small shape will flash whenever the user taps. There will also be a submit button which, when pressed, may either prompt the user to enter the duration of the last note manually (to account for any possible error in timing the last beats) or simply omit the last click.
### (not confirmed) Loading Screen
This screen might include a progress bar (or will not exist as all)
### Final Rhythm Screen
This screen will display the final rhythm. If I can find a way to make the final rhythm into a downloadable PNG or other image, there will be a button to download the final sheet music. Otherwise, notes may be in x-note format (see readme.md).
## Uses
This program could be used to determine notation for a possible song, drumline, or assist in arranging music. It could also be used for fun!