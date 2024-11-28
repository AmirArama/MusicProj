import matplotlib.pyplot as plt
import numpy as np

# Define the notes for the Circle of Fifths
notes = ["C", "G", "D", "A", "E", "B", "F#", "C#", "Ab", "Eb", "Bb", "F", "C"]

# Equal Temperament angles
equal_angle_increment = 30
equal_temperament = [(note, i * equal_angle_increment) for i, note in enumerate(notes)]

# Just Intonation angles using the precise conversion for fifths intervals
just_angle_increment = 30 * (701.955 / 700)
just_intonation = [(note, i * just_angle_increment) for i, note in enumerate(notes)]

print(equal_temperament)
print(just_intonation)