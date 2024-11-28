
# Define the notes for the Circle of Fifths
notes = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13"]

# Equal Temperament angles
equal_angle_increment = 30
equal_temperament = [(note, i * equal_angle_increment) for i, note in enumerate(notes)]

# Just Intonation angles using the precise conversion for fifths intervals
just_angle_increment = 30 * (701.955 / 700)
just_intonation = [(note, i * just_angle_increment) for i, note in enumerate(notes)]

print(equal_temperament)
print(just_intonation)

first_arc = [('1', 0), ('2', 30), ('3', 60), ('4', 90), ('5', 120), ('6', 150), ('7', 180), ('8', 210), ('9', 240), ('10', 270), ('11', 300), ('12', 330), ('13', 360)]
second_arc = [('1', 0.0), ('2', 30.0837), ('3', 60.1675), ('4', 90.2513), ('5', 120.3351), 
              ('6', 150.4189), ('7', 180.5027), ('8', 210.5865), ('9', 240.6702), 
              ('10', 270.7540), ('11', 300.8378), ('12', 330.9216), ('13', 361.0054)]