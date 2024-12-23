chromatic_scale_sharp = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
chromatic_scale_flat = ["C", "Db", "D", "Eb", "E", "F", "Gb", "G", "Ab", "A", "Bb", "B"]

jschromatic_scale_sharp = ["C", "C_sharp", "D", "D_sharp", "E", "F", "F_sharp", "G", "G_sharp", "A", "A_sharp", "B"]
jschromatic_scale_flat = ["C", "D_flat", "D", "E_flat", "E", "F", "G_flat", "G", "A_flat", "A", "B_flat", "B"]

open_string_notes = [("E",4,4),("B",11,3),("G",7,3),("D",2,3),("A",9,2),("E",4,2)]

fretboard_coordinates = [
    {'string': '1', 'fret': '0', 'x': -72.0, 'y': 2},
    {'string': '2', 'fret': '0', 'x': -72.0, 'y': 112},
    {'string': '3', 'fret': '0', 'x': -72.0, 'y': 222},
    {'string': '4', 'fret': '0', 'x': -72.0, 'y': 332},
    {'string': '5', 'fret': '0', 'x': -72.0, 'y': 442},
    {'string': '6', 'fret': '0', 'x': -72.0, 'y': 552},
    {'string': '1', 'fret': '1', 'x': 76.0, 'y': 2},
    {'string': '2', 'fret': '1', 'x': 76.0, 'y': 112},
    {'string': '3', 'fret': '1', 'x': 76.0, 'y': 222},
    {'string': '4', 'fret': '1', 'x': 76.0, 'y': 332},
    {'string': '5', 'fret': '1', 'x': 76.0, 'y': 442},
    {'string': '6', 'fret': '1', 'x': 76.0, 'y': 552},
    {'string': '1', 'fret': '2', 'x': 224.0, 'y': 2},
    {'string': '2', 'fret': '2', 'x': 224.0, 'y': 112},
    {'string': '3', 'fret': '2', 'x': 224.0, 'y': 222},
    {'string': '4', 'fret': '2', 'x': 224.0, 'y': 332},
    {'string': '5', 'fret': '2', 'x': 224.0, 'y': 442},
    {'string': '6', 'fret': '2', 'x': 224.0, 'y': 552},
    {'string': '1', 'fret': '3', 'x': 372.0, 'y': 2},
    {'string': '2', 'fret': '3', 'x': 372.0, 'y': 112},
    {'string': '3', 'fret': '3', 'x': 372.0, 'y': 222},
    {'string': '4', 'fret': '3', 'x': 372.0, 'y': 332},
    {'string': '5', 'fret': '3', 'x': 372.0, 'y': 442},
    {'string': '6', 'fret': '3', 'x': 372.0, 'y': 552},
    {'string': '1', 'fret': '4', 'x': 520.0, 'y': 2},
    {'string': '2', 'fret': '4', 'x': 520.0, 'y': 112},
    {'string': '3', 'fret': '4', 'x': 520.0, 'y': 222},
    {'string': '4', 'fret': '4', 'x': 520.0, 'y': 332},
    {'string': '5', 'fret': '4', 'x': 520.0, 'y': 442},
    {'string': '6', 'fret': '4', 'x': 520.0, 'y': 552},
    {'string': '1', 'fret': '5', 'x': 668.0, 'y': 2},
    {'string': '2', 'fret': '5', 'x': 668.0, 'y': 112},
    {'string': '3', 'fret': '5', 'x': 668.0, 'y': 222},
    {'string': '4', 'fret': '5', 'x': 668.0, 'y': 332},
    {'string': '5', 'fret': '5', 'x': 668.0, 'y': 442},
    {'string': '6', 'fret': '5', 'x': 668.0, 'y': 552},
    {'string': '1', 'fret': '6', 'x': 816.0, 'y': 2},
    {'string': '2', 'fret': '6', 'x': 816.0, 'y': 112},
    {'string': '3', 'fret': '6', 'x': 816.0, 'y': 222},
    {'string': '4', 'fret': '6', 'x': 816.0, 'y': 332},
    {'string': '5', 'fret': '6', 'x': 816.0, 'y': 442},
    {'string': '6', 'fret': '6', 'x': 816.0, 'y': 552},
    {'string': '1', 'fret': '7', 'x': 964.0, 'y': 2},
    {'string': '2', 'fret': '7', 'x': 964.0, 'y': 112},
    {'string': '3', 'fret': '7', 'x': 964.0, 'y': 222},
    {'string': '4', 'fret': '7', 'x': 964.0, 'y': 332},
    {'string': '5', 'fret': '7', 'x': 964.0, 'y': 442},
    {'string': '6', 'fret': '7', 'x': 964.0, 'y': 552},
    {'string': '1', 'fret': '8', 'x': 1112.0, 'y': 2},
    {'string': '2', 'fret': '8', 'x': 1112.0, 'y': 112},
    {'string': '3', 'fret': '8', 'x': 1112.0, 'y': 222},
    {'string': '4', 'fret': '8', 'x': 1112.0, 'y': 332},
    {'string': '5', 'fret': '8', 'x': 1112.0, 'y': 442},
    {'string': '6', 'fret': '8', 'x': 1112.0, 'y': 552},
    {'string': '1', 'fret': '9', 'x': 1260.0, 'y': 2},
    {'string': '2', 'fret': '9', 'x': 1260.0, 'y': 112},
    {'string': '3', 'fret': '9', 'x': 1260.0, 'y': 222},
    {'string': '4', 'fret': '9', 'x': 1260.0, 'y': 332},
    {'string': '5', 'fret': '9', 'x': 1260.0, 'y': 442},
    {'string': '6', 'fret': '9', 'x': 1260.0, 'y': 552},
    {'string': '1', 'fret': '10', 'x': 1408.0, 'y': 2},
    {'string': '2', 'fret': '10', 'x': 1408.0, 'y': 112},
    {'string': '3', 'fret': '10', 'x': 1408.0, 'y': 222},
    {'string': '4', 'fret': '10', 'x': 1408.0, 'y': 332},
    {'string': '5', 'fret': '10', 'x': 1408.0, 'y': 442},
    {'string': '6', 'fret': '10', 'x': 1408.0, 'y': 552},
    {'string': '1', 'fret': '11', 'x': 1556.0, 'y': 2},
    {'string': '2', 'fret': '11', 'x': 1556.0, 'y': 112},
    {'string': '3', 'fret': '11', 'x': 1556.0, 'y': 222},
    {'string': '4', 'fret': '11', 'x': 1556.0, 'y': 332},
    {'string': '5', 'fret': '11', 'x': 1556.0, 'y': 442},
    {'string': '6', 'fret': '11', 'x': 1556.0, 'y': 552},
    {'string': '1', 'fret': '12', 'x': 1704.0, 'y': 2},
    {'string': '2', 'fret': '12', 'x': 1704.0, 'y': 112},
    {'string': '3', 'fret': '12', 'x': 1704.0, 'y': 222},
    {'string': '4', 'fret': '12', 'x': 1704.0, 'y': 332},
    {'string': '5', 'fret': '12', 'x': 1704.0, 'y': 442},
    {'string': '6', 'fret': '12', 'x': 1704.0, 'y': 552},
    {'string': '1', 'fret': '13', 'x': 1852.0, 'y': 2},
    {'string': '2', 'fret': '13', 'x': 1852.0, 'y': 112},
    {'string': '3', 'fret': '13', 'x': 1852.0, 'y': 222},
    {'string': '4', 'fret': '13', 'x': 1852.0, 'y': 332},
    {'string': '5', 'fret': '13', 'x': 1852.0, 'y': 442},
    {'string': '6', 'fret': '13', 'x': 1852.0, 'y': 552},
    {'string': '1', 'fret': '14', 'x': 2000.0, 'y': 2},
    {'string': '2', 'fret': '14', 'x': 2000.0, 'y': 112},
    {'string': '3', 'fret': '14', 'x': 2000.0, 'y': 222},
    {'string': '4', 'fret': '14', 'x': 2000.0, 'y': 332},
    {'string': '5', 'fret': '14', 'x': 2000.0, 'y': 442},
    {'string': '6', 'fret': '14', 'x': 2000.0, 'y': 552},
    {'string': '1', 'fret': '15', 'x': 2148.0, 'y': 2},
    {'string': '2', 'fret': '15', 'x': 2148.0, 'y': 112},
    {'string': '3', 'fret': '15', 'x': 2148.0, 'y': 222},
    {'string': '4', 'fret': '15', 'x': 2148.0, 'y': 332},
    {'string': '5', 'fret': '15', 'x': 2148.0, 'y': 442},
    {'string': '6', 'fret': '15', 'x': 2148.0, 'y': 552},
    {'string': '1', 'fret': '16', 'x': 2296.0, 'y': 2},
    {'string': '2', 'fret': '16', 'x': 2296.0, 'y': 112},
    {'string': '3', 'fret': '16', 'x': 2296.0, 'y': 222},
    {'string': '4', 'fret': '16', 'x': 2296.0, 'y': 332},
    {'string': '5', 'fret': '16', 'x': 2296.0, 'y': 442},
    {'string': '6', 'fret': '16', 'x': 2296.0, 'y': 552},
    {'string': '1', 'fret': '17', 'x': 2444.0, 'y': 2},
    {'string': '2', 'fret': '17', 'x': 2444.0, 'y': 112},
    {'string': '3', 'fret': '17', 'x': 2444.0, 'y': 222},
    {'string': '4', 'fret': '17', 'x': 2444.0, 'y': 332},
    {'string': '5', 'fret': '17', 'x': 2444.0, 'y': 442},
    {'string': '6', 'fret': '17', 'x': 2444.0, 'y': 552},
    {'string': '1', 'fret': '18', 'x': 2592.0, 'y': 2},
    {'string': '2', 'fret': '18', 'x': 2592.0, 'y': 112},
    {'string': '3', 'fret': '18', 'x': 2592.0, 'y': 222},
    {'string': '4', 'fret': '18', 'x': 2592.0, 'y': 332},
    {'string': '5', 'fret': '18', 'x': 2592.0, 'y': 442},
    {'string': '6', 'fret': '18', 'x': 2592.0, 'y': 552},
    {'string': '1', 'fret': '19', 'x': 2740.0, 'y': 2},
    {'string': '2', 'fret': '19', 'x': 2740.0, 'y': 112},
    {'string': '3', 'fret': '19', 'x': 2740.0, 'y': 222},
    {'string': '4', 'fret': '19', 'x': 2740.0, 'y': 332},
    {'string': '5', 'fret': '19', 'x': 2740.0, 'y': 442},
    {'string': '6', 'fret': '19', 'x': 2740.0, 'y': 552},
    {'string': '1', 'fret': '20', 'x': 2888.0, 'y': 2},
    {'string': '2', 'fret': '20', 'x': 2888.0, 'y': 112},
    {'string': '3', 'fret': '20', 'x': 2888.0, 'y': 222},
    {'string': '4', 'fret': '20', 'x': 2888.0, 'y': 332},
    {'string': '5', 'fret': '20', 'x': 2888.0, 'y': 442},
    {'string': '6', 'fret': '20', 'x': 2888.0, 'y': 552},
    {'string': '1', 'fret': '21', 'x': 3036.0, 'y': 2},
    {'string': '2', 'fret': '21', 'x': 3036.0, 'y': 112},
    {'string': '3', 'fret': '21', 'x': 3036.0, 'y': 222},
    {'string': '4', 'fret': '21', 'x': 3036.0, 'y': 332},
    {'string': '5', 'fret': '21', 'x': 3036.0, 'y': 442},
    {'string': '6', 'fret': '21', 'x': 3036.0, 'y': 552},
    {'string': '1', 'fret': '22', 'x': 3184.0, 'y': 2},
    {'string': '2', 'fret': '22', 'x': 3184.0, 'y': 112},
    {'string': '3', 'fret': '22', 'x': 3184.0, 'y': 222},
    {'string': '4', 'fret': '22', 'x': 3184.0, 'y': 332},
    {'string': '5', 'fret': '22', 'x': 3184.0, 'y': 442},
    {'string': '6', 'fret': '22', 'x': 3184.0, 'y': 552}
]

fretboard_frequency = [  
    {'string': 1, 'fret': 0, 'frequency': 329.63}, 
    {'string': 1, 'fret': 1, 'frequency': 349.23}, 
    {'string': 1, 'fret': 2, 'frequency': 370.0}, 
    {'string': 1, 'fret': 3, 'frequency': 392.0}, 
    {'string': 1, 'fret': 4, 'frequency': 415.31}, 
    {'string': 1, 'fret': 5, 'frequency': 440.0}, 
    {'string': 1, 'fret': 6, 'frequency': 466.17}, 
    {'string': 1, 'fret': 7, 'frequency': 493.89}, 
    {'string': 1, 'fret': 8, 'frequency': 523.26}, 
    {'string': 1, 'fret': 9, 'frequency': 554.37}, 
    {'string': 1, 'fret': 10, 'frequency': 587.33}, 
    {'string': 1, 'fret': 11, 'frequency': 622.26}, 
    {'string': 1, 'fret': 12, 'frequency': 659.26}, 
    {'string': 1, 'fret': 13, 'frequency': 698.46}, 
    {'string': 1, 'fret': 14, 'frequency': 739.99}, 
    {'string': 1, 'fret': 15, 'frequency': 784.0}, 
    {'string': 1, 'fret': 16, 'frequency': 830.62}, 
    {'string': 1, 'fret': 17, 'frequency': 880.01}, 
    {'string': 1, 'fret': 18, 'frequency': 932.33}, 
    {'string': 1, 'fret': 19, 'frequency': 987.77}, 
    {'string': 1, 'fret': 20, 'frequency': 1046.51}, 
    {'string': 1, 'fret': 21, 'frequency': 1108.74}, 
    {'string': 1, 'fret': 22, 'frequency': 1174.67}, 
    {'string': 2, 'fret': 0, 'frequency': 246.94}, 
    {'string': 2, 'fret': 1, 'frequency': 261.62}, 
    {'string': 2, 'fret': 2, 'frequency': 277.18}, 
    {'string': 2, 'fret': 3, 'frequency': 293.66}, 
    {'string': 2, 'fret': 4, 'frequency': 311.12}, 
    {'string': 2, 'fret': 5, 'frequency': 329.63}, 
    {'string': 2, 'fret': 6, 'frequency': 349.23}, 
    {'string': 2, 'fret': 7, 'frequency': 369.99}, 
    {'string': 2, 'fret': 8, 'frequency': 391.99}, 
    {'string': 2, 'fret': 9, 'frequency': 415.3}, 
    {'string': 2, 'fret': 10, 'frequency': 440.0}, 
    {'string': 2, 'fret': 11, 'frequency': 466.16}, 
    {'string': 2, 'fret': 12, 'frequency': 493.88}, 
    {'string': 2, 'fret': 13, 'frequency': 523.25}, 
    {'string': 2, 'fret': 14, 'frequency': 554.36}, 
    {'string': 2, 'fret': 15, 'frequency': 587.33}, 
    {'string': 2, 'fret': 16, 'frequency': 622.25}, 
    {'string': 2, 'fret': 17, 'frequency': 659.25}, 
    {'string': 2, 'fret': 18, 'frequency': 698.45}, 
    {'string': 2, 'fret': 19, 'frequency': 739.98}, 
    {'string': 2, 'fret': 20, 'frequency': 783.99}, 
    {'string': 2, 'fret': 21, 'frequency': 830.6}, 
    {'string': 2, 'fret': 22, 'frequency': 879.99}, 
    {'string': 3, 'fret': 0, 'frequency': 196.0}, 
    {'string': 3, 'fret': 1, 'frequency': 207.65}, 
    {'string': 3, 'fret': 2, 'frequency': 220.0}, 
    {'string': 3, 'fret': 3, 'frequency': 233.08}, 
    {'string': 3, 'fret': 4, 'frequency': 246.94}, 
    {'string': 3, 'fret': 5, 'frequency': 261.63}, 
    {'string': 3, 'fret': 6, 'frequency': 277.19}, 
    {'string': 3, 'fret': 7, 'frequency': 293.67}, 
    {'string': 3, 'fret': 8, 'frequency': 311.13}, 
    {'string': 3, 'fret': 9, 'frequency': 329.63}, 
    {'string': 3, 'fret': 10, 'frequency': 349.23}, 
    {'string': 3, 'fret': 11, 'frequency': 370.0}, 
    {'string': 3, 'fret': 12, 'frequency': 392.0}, 
    {'string': 3, 'fret': 13, 'frequency': 415.31}, 
    {'string': 3, 'fret': 14, 'frequency': 440.01}, 
    {'string': 3, 'fret': 15, 'frequency': 466.17}, 
    {'string': 3, 'fret': 16, 'frequency': 493.89}, 
    {'string': 3, 'fret': 17, 'frequency': 523.26}, 
    {'string': 3, 'fret': 18, 'frequency': 554.37}, 
    {'string': 3, 'fret': 19, 'frequency': 587.34}, 
    {'string': 3, 'fret': 20, 'frequency': 622.26}, 
    {'string': 3, 'fret': 21, 'frequency': 659.26}, 
    {'string': 3, 'fret': 22, 'frequency': 698.46}, 
    {'string': 4, 'fret': 0, 'frequency': 146.83}, 
    {'string': 4, 'fret': 1, 'frequency': 155.56}, 
    {'string': 4, 'fret': 2, 'frequency': 164.81}, 
    {'string': 4, 'fret': 3, 'frequency': 174.61}, 
    {'string': 4, 'fret': 4, 'frequency': 184.99}, 
    {'string': 4, 'fret': 5, 'frequency': 195.99}, 
    {'string': 4, 'fret': 6, 'frequency': 207.65}, 
    {'string': 4, 'fret': 7, 'frequency': 220.0}, 
    {'string': 4, 'fret': 8, 'frequency': 233.08}, 
    {'string': 4, 'fret': 9, 'frequency': 246.94}, 
    {'string': 4, 'fret': 10, 'frequency': 261.62}, 
    {'string': 4, 'fret': 11, 'frequency': 277.18}, 
    {'string': 4, 'fret': 12, 'frequency': 293.66}, 
    {'string': 4, 'fret': 13, 'frequency': 311.12}, 
    {'string': 4, 'fret': 14, 'frequency': 329.62}, 
    {'string': 4, 'fret': 15, 'frequency': 349.22}, 
    {'string': 4, 'fret': 16, 'frequency': 369.99}, 
    {'string': 4, 'fret': 17, 'frequency': 391.99}, 
    {'string': 4, 'fret': 18, 'frequency': 415.3}, 
    {'string': 4, 'fret': 19, 'frequency': 439.99}, 
    {'string': 4, 'fret': 20, 'frequency': 466.16}, 
    {'string': 4, 'fret': 21, 'frequency': 493.88}, 
    {'string': 4, 'fret': 22, 'frequency': 523.24}, 
    {'string': 5, 'fret': 0, 'frequency': 110.0}, 
    {'string': 5, 'fret': 1, 'frequency': 116.54}, 
    {'string': 5, 'fret': 2, 'frequency': 123.47}, 
    {'string': 5, 'fret': 3, 'frequency': 130.81}, 
    {'string': 5, 'fret': 4, 'frequency': 138.59}, 
    {'string': 5, 'fret': 5, 'frequency': 146.83}, 
    {'string': 5, 'fret': 6, 'frequency': 155.56}, 
    {'string': 5, 'fret': 7, 'frequency': 164.81}, 
    {'string': 5, 'fret': 8, 'frequency': 174.61}, 
    {'string': 5, 'fret': 9, 'frequency': 185.0}, 
    {'string': 5, 'fret': 10, 'frequency': 196.0}, 
    {'string': 5, 'fret': 11, 'frequency': 207.65}, 
    {'string': 5, 'fret': 12, 'frequency': 220.0}, 
    {'string': 5, 'fret': 13, 'frequency': 233.08}, 
    {'string': 5, 'fret': 14, 'frequency': 246.94}, 
    {'string': 5, 'fret': 15, 'frequency': 261.63}, 
    {'string': 5, 'fret': 16, 'frequency': 277.18}, 
    {'string': 5, 'fret': 17, 'frequency': 293.66}, 
    {'string': 5, 'fret': 18, 'frequency': 311.13}, 
    {'string': 5, 'fret': 19, 'frequency': 329.63}, 
    {'string': 5, 'fret': 20, 'frequency': 349.23}, 
    {'string': 5, 'fret': 21, 'frequency': 369.99}, 
    {'string': 5, 'fret': 22, 'frequency': 392.0}, 
    {'string': 6, 'fret': 0, 'frequency': 82.41}, 
    {'string': 6, 'fret': 1, 'frequency': 87.31}, 
    {'string': 6, 'fret': 2, 'frequency': 92.5}, 
    {'string': 6, 'fret': 3, 'frequency': 98.0}, 
    {'string': 6, 'fret': 4, 'frequency': 103.83}, 
    {'string': 6, 'fret': 5, 'frequency': 110.0}, 
    {'string': 6, 'fret': 6, 'frequency': 116.55}, 
    {'string': 6, 'fret': 7, 'frequency': 123.48}, 
    {'string': 6, 'fret': 8, 'frequency': 130.82}, 
    {'string': 6, 'fret': 9, 'frequency': 138.6}, 
    {'string': 6, 'fret': 10, 'frequency': 146.84}, 
    {'string': 6, 'fret': 11, 'frequency': 155.57}, 
    {'string': 6, 'fret': 12, 'frequency': 164.82}, 
    {'string': 6, 'fret': 13, 'frequency': 174.62}, 
    {'string': 6, 'fret': 14, 'frequency': 185.0}, 
    {'string': 6, 'fret': 15, 'frequency': 196.01}, 
    {'string': 6, 'fret': 16, 'frequency': 207.66}, 
    {'string': 6, 'fret': 17, 'frequency': 220.01}, 
    {'string': 6, 'fret': 18, 'frequency': 233.09}, 
    {'string': 6, 'fret': 19, 'frequency': 246.95}, 
    {'string': 6, 'fret': 20, 'frequency': 261.64}, 
    {'string': 6, 'fret': 21, 'frequency': 277.19}, 
    {'string': 6, 'fret': 22, 'frequency': 293.68}
]


# A Sneaky Bug Fix
# In some cases, the first inversion found on the fretboard is not the root inversion. 
# This happens when the notes needed to build the root inversion are missing on the fretboard. 
# As a result, it becomes impossible to produce and position subsequent inversions correctly.
# 
# By supplying virtual notes outside the physical fretboard range, we address this issue, 
# ensuring that all inversions can be calculated and placed properly.

fake_notes_sharp = {
    # Virtual notes for octave 2 on lower strings
    (6, 'C2'): {'note': 'C','fret': -1, 'x': -1, 'y': -1, 'octave': 2, 'frequency': -1},
    (6, 'C#2'): {'note': 'C#','fret': -1, 'x': -1, 'y': -1, 'octave': 2, 'frequency': -1},
    (6, 'D2'): {'note': 'D','fret': -1, 'x': -1, 'y': -1, 'octave': 2, 'frequency': -1},
    (6, 'D#2'): {'note': 'D#','fret': -1, 'x': -1, 'y': -1, 'octave': 2, 'frequency': -1}
}
fake_notes_flat = {
    # Virtual notes for octave 2 on lower strings
    (6, 'C2'): {'note': 'C','fret': -1, 'x': -1, 'y': -1, 'octave': 2, 'frequency': -1},
    (6, 'Db2'): {'note': 'Db','fret': -1, 'x': -1, 'y': -1, 'octave': 2, 'frequency': -1},
    (6, 'D2'): {'note': 'D','fret': -1, 'x': -1, 'y': -1, 'octave': 2, 'frequency': -1},
    (6, 'Eb2'): {'note': 'Eb','fret': -1, 'x': -1, 'y': -1, 'octave': 2, 'frequency': -1}
}

def generate_strings_notes_22frets(type_):
    global chromatic_scale_sharp
    global chromatic_scale_flat
    global jschromatic_scale_sharp
    global jschromatic_scale_flat
    if type_=="flat":
        chromatic_notes = chromatic_scale_flat
        jschromatic_notes = jschromatic_scale_flat
        fake_notes = fake_notes_flat
    elif type_=="sharp":
        chromatic_notes = chromatic_scale_sharp
        jschromatic_notes = jschromatic_scale_sharp
        fake_notes = fake_notes_sharp
    else:
        print("fretboard notes type not supported")
        return

    fretboardNotes = {}
    new_fretboard = {}
    for i in range(6):
        string = []
        startNote = open_string_notes[i][0]
        startNoteIdx = open_string_notes[i][1]
        startOctave = open_string_notes[i][2]
        k = startNoteIdx
        for j in range(23):
            if k%12 == 0:
                k = 0
                startOctave = startOctave + 1
            matching_element = next((item for item in fretboard_coordinates if item['string'] == str(i+1) and item['fret'] == str(j)), None)
            if matching_element:
                x = matching_element['x']
                y = matching_element['y']
            matching_element2 = next((item for item in fretboard_frequency if item['string'] == i+1 and item['fret'] == j), None)
            if matching_element2:
                freq = matching_element2['frequency']
            info =  {'note':chromatic_notes[k],'jsnote':jschromatic_notes[k], 'fret': j , 'x': x, 'y': y, 'octave':startOctave,'frequency': freq} 
            new_fretboard[(i,chromatic_notes[k]+str(startOctave))] = info
            k = k + 1
    new_fretboard.update(fake_notes)        
    return new_fretboard

fretboard_data_sharp = generate_strings_notes_22frets('sharp')
fretboard_data_flat = generate_strings_notes_22frets('flat')

#print(fretboard_data) 

def get_note_data(string, note_with_octave):
    fdata = fretboard_data_flat
    if len(note_with_octave) > 1:
        if note_with_octave[1] == "#":
            fdata = fretboard_data_sharp
    key = (string, note_with_octave)  # Construct the tuple key
    return fdata.get(key, None)  # Return the value if it exists, else None

def get_root_note(note):
    fdata = fretboard_data_flat
    if len(note) > 1:
        if note[1] == "#":
            fdata = fretboard_data_sharp
    return [key for key in fdata.keys() if key[1].startswith(note)]
#print(get_root_note('C'))

# Example usage
'''
string = 5
note_with_octave = 'G#3'

result = get_note_data(string, note_with_octave)
if result:
    print(f"Data for String {string}, Note {note_with_octave}: {result}")
else:
    print(f"No data found for String {string}, Note {note_with_octave}")
'''
