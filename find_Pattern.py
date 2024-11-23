from filter_by_note import filter_by_note

class FretboardPatternSearch:
    def __init__(self, patterns):
        # Convert each pattern list to a set for unordered matching
        self.patterns = {pattern: set(notes) for pattern, notes in patterns.items()}
        self.found_patterns = {pattern: False for pattern in patterns}  # Track found patterns
        self.current_selection = set()
        self.current_pattern = None
        self.completed = False

    def press_note(self, note):
        # If all patterns are found, mark the task as completed
        if all(self.found_patterns.values()):
            self.completed = True
            print("All patterns found! Task completed.")
            return

        # Check if we are already in a pattern search or need to reset
        if self.current_pattern is None:
            self._start_new_pattern(note)
        else:
            self._continue_pattern(note)

    def _start_new_pattern(self, note):
        # Start checking for a new pattern
        for pattern, notes in self.patterns.items():
            if note in notes and not self.found_patterns[pattern]:  # Start new search if note matches
                self.current_pattern = pattern
                self.current_selection = {note}
                print(f"Starting pattern search for {pattern} with note '{note}'")
                return
        # If no matching pattern is found, ignore the note and do not reset
        print(f"Ignoring note '{note}', no matching pattern found.")
    
    def _continue_pattern(self, note):
        # Continue adding notes if they belong to the current pattern's note set
        if note in self.patterns[self.current_pattern]:
            self.current_selection.add(note)
            print(f"Note '{note}' added to current pattern '{self.current_pattern}'")
            # Check if the pattern is completed
            if self.current_selection == self.patterns[self.current_pattern]:
                self.found_patterns[self.current_pattern] = True
                print(f"Pattern '{self.current_pattern}' found!")
                self._reset_selection()
        else:
            # Ignore unrelated notes instead of resetting
            print(f"Note '{note}' is not part of the current pattern '{self.current_pattern}', ignoring.")

    def _reset_selection(self):
        # Reset the current pattern search
        self.current_pattern = None
        self.current_selection = set()


'''
# Define patterns to search for, each with 3 elements in any order
patterns = {
    "pattern1": ["A", "B", "C"],
    "pattern2": ["D", "E", "F"],
    "pattern3": ["G", "A", "B"]
}

# Create the fretboard pattern search instance
fretboard_search = FretboardPatternSearch(patterns)

# Example usage simulating note presses
fretboard_search.press_note("B")  # Starts pattern1
fretboard_search.press_note("C")  # Continues pattern1
fretboard_search.press_note("F")  # Unrelated note, ignored
fretboard_search.press_note("A")  # Completes pattern1

fretboard_search.press_note("E")  # Starts pattern2
fretboard_search.press_note("G")  # Unrelated note, ignored
fretboard_search.press_note("D")  # Continues pattern2
fretboard_search.press_note("F")  # Completes pattern2

# Check if all patterns were found
if fretboard_search.completed:
    print("All patterns were successfully found.")
'''