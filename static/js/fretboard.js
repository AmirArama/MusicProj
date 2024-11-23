let bufferSize = 4096; // Keep the fftSize as 2048 for better frequency resolution
let targetBufferSize = 4096; // Set target buffer size to match aubio's requirement
const silenceThreshold = 0.01;

function setup() {
    audioContext = new (window.AudioContext || window.webkitAudioContext)();
    navigator.mediaDevices.getUserMedia({ audio: true })
        .then(stream => {
            const source = audioContext.createMediaStreamSource(stream);
            analyser = audioContext.createAnalyser();
            analyser.fftSize = bufferSize;
            source.connect(analyser);

            // Start sending audio data to the server
            sendAudioToServer();
        })
        .catch(error => console.error("Error accessing microphone:", error));
}

function calculateRMS(buffer) {
    let sum = 0;
    for (let i = 0; i < buffer.length; i++) {
        sum += buffer[i] * buffer[i];
    }
    return Math.sqrt(sum / buffer.length);
}


function sendAudioToServer() {
    setInterval(() => {
        const buffer = new Float32Array(analyser.fftSize);
        analyser.getFloatTimeDomainData(buffer);

        // Slice buffer to 1024 samples to match aubio's requirement
        const audioData = Array.from(buffer.slice(0, targetBufferSize));

        // Calculate the RMS (Root Mean Square) of the buffer
        const rms = calculateRMS(buffer);

        // Return early if RMS is below the silence threshold
        if (rms <= silenceThreshold) {
            console.log("Buffer is silent, skipping...");
            return;  // Exit the function without sending data
        }


        // Send data to Flask endpoint
        fetch('/analyze-pitch', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ audioData })
        })
        .then(response => response.json())
        .then(data => {
            if (data.note) {
                console.log(`Detected Note: ${data.note.note}`);
                updateNote(data.note.note);
            }
        })
        .catch(error => console.error('Error:', error));
    }, 500); // Adjust frequency as needed
}
