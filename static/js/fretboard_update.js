function updateNote(noteId) {
    console.log("Trying to update a note: ",noteId)
    searchForActiveNote(noteId);
}

function searchForActiveNote(noteId) {
    // Select all elements whose ID starts with the provided noteId
    const elements = document.querySelectorAll(`[id^="${noteId}_"]`);
    console.log(elements)
    
    // Apply the desired active style to each element
    elements.forEach(element => {
        // Toggle a class or apply styles as needed
        toggleNoteActiveSilent(element.id);
        console.log("----->",element.id)
    });
}

function toggleNoteActive(noteId) {
    let str = noteId;
    let tone = str.split("_")[0]; 
    const noteElement = document.getElementById(noteId);

    // Add the active class for the scaling effect
    noteElement.classList.add('active');
    console.log(noteId)

    const synth = new Tone.Synth().toDestination();
    synth.triggerAttackRelease(tone, ".1s");

    //addNotePress(noteId);

    // Remove the active class after 2 seconds
    setTimeout(() => {
        noteElement.classList.remove('active');
    }, 2000);
}

function toggleNoteActiveSilent(noteId) {
    const noteElement = document.getElementById(noteId);
    //console.log("ssssss",noteElement)

    noteElement.classList.add('active');
    console.log("++++++:", noteId)
    // Remove the active class after 2 seconds
    setTimeout(() => {
        noteElement.classList.remove('active');
    }, 100);
}