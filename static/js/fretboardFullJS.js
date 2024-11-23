let audioContext;
let mic;
let analyser;
let pitchFinder;
const SMOOTHING_FACTOR = 0.2;
const MIN_FREQUENCY = 0; // Minimum frequency for guitar
const MAX_FREQUENCY = 1300; // Upper limit for guitar notes
let previousFrequency = null;
let frequencyBuffer = [];
const BUFFER_SIZE = 5;
/*
const notes = [
    { note: "E", frequency: 82.41 },
    { note: "A", frequency: 110.00 },
    { note: "D", frequency: 146.83 },
    { note: "G", frequency: 196.00 },
    { note: "B", frequency: 246.94 },
    { note: "E", frequency: 329.63 }
];
*/
const baseNotes = [
    { note: "E", frequency: 82.41, octave: 2 },  // E2 (Low E string)
    { note: "A", frequency: 110.00, octave: 2 }, // A2
    { note: "D", frequency: 146.83, octave: 3 }, // D3
    { note: "G", frequency: 196.00, octave: 3 }, // G3
    { note: "B", frequency: 246.94, octave: 3 }, // B3
    { note: "E", frequency: 329.63, octave: 4 }  // E4 (High E string)
];

const fretCount = 22;
const notes = [];

// Helper function to get the note name with octave based on frequency
function getNoteName(frequency) {
    const noteNames = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"];
    const noteIndex = Math.round(12 * (Math.log2(frequency / 440))) + 69; // MIDI note number
    const octave = Math.floor(noteIndex / 12) - 1;
    const note = noteNames[noteIndex % 12];
    return `${note}${octave}`;
}

baseNotes.forEach((baseNote, stringIndex) => {
    for (let fret = 0; fret <= fretCount; fret++) {
        const frequency = baseNote.frequency * Math.pow(2, fret / 12);
        const noteName = getNoteName(frequency);
        
        notes.push({ note: noteName, frequency: parseFloat(frequency.toFixed(2)) });
    }
});

console.log(notes);



console.log(typeof PitchFinder); // Should output "object" if properly loaded


// Setup function to initialize audio context and mic input
function setup() {
    noCanvas();
    audioContext = new (window.AudioContext || window.webkitAudioContext)();
    console.log("Starting Note detection.")

    // Initialize PitchFinder YIN algorithm
    if (typeof PitchFinder !== 'undefined' && PitchFinder.YIN) {
        pitchFinder = new PitchFinder.YIN({ sampleRate: audioContext.sampleRate });
    } else {
        console.error("PitchFinder is not available in the global scope. Make sure pitchfinder.bundle.js is loaded.");
        return;
    }

    navigator.mediaDevices.getUserMedia({ audio: true })
        .then(stream => {
            const source = audioContext.createMediaStreamSource(stream);
            analyser = audioContext.createAnalyser();
            analyser.fftSize = 8192;
            source.connect(analyser);

            detectPitch();
            console.log("Detecting!!!")
        })
        .catch(error => console.error("Error accessing microphone:", error));
}

// Main pitch detection loop
function detectPitch() {
    const buffer = new Float32Array(analyser.fftSize);
    analyser.getFloatTimeDomainData(buffer);

    const frequency = pitchFinder(buffer);

    if (frequency && frequency >= MIN_FREQUENCY && frequency <= MAX_FREQUENCY) {
        frequencyBuffer.push(frequency);
        if (frequencyBuffer.length > BUFFER_SIZE) frequencyBuffer.shift();

        const averagedFrequency = getAverageFrequency(frequencyBuffer);
        const smoothedFrequency = smoothFrequency(averagedFrequency);
        const correctedFrequency = correctOctaveError(smoothedFrequency);
        const closestNote = getClosestNote(correctedFrequency);
        const theModuloOffset = getOffset(correctedFrequency);
        const theOffset = correctedFrequency-closestNote.frequency;

        updateNote(closestNote.note);

        console.log(`Frequency: ${correctedFrequency.toFixed(2)} Hz, Note: ${closestNote.note}`);
        console.log(`Closes Note Frequency: ${closestNote.frequency}, offset: ${theOffset}, (${theModuloOffset})`);
    } else {
        //console.log("Frequency out of range or invalid");
    }

    requestAnimationFrame(detectPitch);
}

// Calculate the average frequency from the buffer
function getAverageFrequency(buffer) {
    return buffer.reduce((sum, freq) => sum + freq, 0) / buffer.length;
}

// Smooth the frequency using a weighted average
function smoothFrequency(frequency) {
    if (!previousFrequency) {
        previousFrequency = frequency;
    }
    const smoothedFrequency = previousFrequency * (1 - SMOOTHING_FACTOR) + frequency * SMOOTHING_FACTOR;
    previousFrequency = smoothedFrequency;
    return smoothedFrequency;
}

// Adjust for octave errors
function correctOctaveError(frequency) {
    const closestNote = getClosestNote(frequency);
    const expectedFrequency = closestNote.frequency;

    if (frequency > expectedFrequency * 1.8 && frequency < expectedFrequency * 2.2) {
        frequency /= 2;
    } else if (frequency < expectedFrequency * 0.55 && frequency > expectedFrequency * 0.45) {
        frequency *= 2;
    }
    return frequency;
}

// Find the closest note based on frequency
function getClosestNote(frequency) {
    return notes.reduce((prev, curr) =>
        Math.abs(curr.frequency - frequency) < Math.abs(prev.frequency - frequency) ? curr : prev
    );
}

function getOffset(frequency){
    const closestNote = getClosestNote(frequency);
    const offset = frequency - closestNote.frequency;

    return Math.round(offset/10)*10;

}
/*
setInterval(() => {
    console.log("will work")
}, 5000);
*/