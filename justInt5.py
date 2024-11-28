# Equal Temperament Circle of Fifths
equal_temperament = []
just_intonation = []
notes = ["C", "G", "D", "A", "E", "B", "F#", "C#", "Ab", "Eb", "Bb", "F","C"]

equal_angle_increment = 30
just_angle_increment = 30 * (701.955 / 700)


# Generate the list for equal temperament
for i, note in enumerate(notes):
    equal_angle = i * equal_angle_increment
    just_angle = i * just_angle_increment
    equal_temperament.append((note, equal_angle))
    just_intonation.append((note, just_angle))

print("Equal Temperament Circle of Fifths:")
print(equal_temperament)

print("\nJust Intonation Circle of Fifths:")
print(just_intonation)


