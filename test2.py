from filter_by_note import filter_by_note, append_coordinates
from fretboard_notes import fretboard_notes
from fretboard_coordinates import fretboard_coordinates


target_note = "A"
filtered_fretboard_notes = filter_by_note(fretboard_notes, target_note)
filtered_fretboard_notes = append_coordinates(filtered_fretboard_notes, fretboard_coordinates)
print(filtered_fretboard_notes)