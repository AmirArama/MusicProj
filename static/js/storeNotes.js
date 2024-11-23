// Object to store the pressed A notes (e.g., { "string_6_fret_5": true })
let aNotePresses = {};

// Function to add the note press to the collection
function addNotePress(noteId) {
    if (!aNotePresses[noteId]) {
        aNotePresses[noteId] = true; // Mark the note as pressed
        console.log(`A note pressed at: ${noteId}`);
    }
    console.log(aNotePresses)
}