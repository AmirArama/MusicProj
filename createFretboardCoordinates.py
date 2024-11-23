# Coordinates generation code
startX = 2 + 148 / 2 - 148
startY = 2
offSetX = 148
offsetY = 110

fretboard_coordinates = {}
for i in range(0, 23):
    for j in range(1, 7):
        stringName = f"string_{j}" 
        fretName = f"fret_{i}"
        fretboard_coordinates[(stringName, fretName)] = (startX + (i) * offSetX, startY + (j-1) * offsetY)
print(fretboard_coordinates)
# Sort the dictionary by fret order (second part of each tuple key)
sorted_fretboard_coordinates = dict(sorted(
    fretboard_coordinates.items(),
    key=lambda x: int(x[0][1].split('_')[1])  # Sort by fret number in "fret_X"
))

# Save to a .py file
with open("fretboard_coordinates.py", "w") as file:
    file.write("fretboard_coordinates = {\n")
    for key, value in sorted_fretboard_coordinates.items():
        file.write(f"    {key}: {value},\n")
    file.write("}\n")

print("Dictionary saved to fretboard_coordinates.py")
