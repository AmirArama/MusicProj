
/*
document.addEventListener('DOMContentLoaded', () => {
    const domInteractiveTime = performance.now();
    console.log(`DOMContentLoaded fired at: ${domInteractiveTime.toFixed(2)} ms`);
});

window.onload = () => {
    const windowLoadTime = performance.now();
    console.log(`window.onload fired at: ${windowLoadTime.toFixed(2)} ms`);
};
*/



// Function to send the current configuration to the backend
function sendConfiguration() {
    const data = {
        note: $('#notesDropdown').val(),
        inversion: $('#inversionDropdown').val(),
        type: $('#typeDropdown').val(),
        stringSet: $('#stringSetDropdown').val(),
        noteInterval: $('#noteIntervalDropdown').val()
    };

    $.ajax({
        url: '/filter',
        type: 'POST',
        contentType: 'application/json',
        data: JSON.stringify(data),
        success: function(response) {
            const filteredData = response.filtered_data; // Get filtered data from the response
            //console.log(filteredData)
            updateFretboard(filteredData);               // Update the fretboard
        },
        error: function(error) {
            console.error('Error fetching filtered data:', error);
        }
    });
}

// Function to update the fretboard based on filtered data
function updateFretboard(filteredData) {

    let x_offset = 200
    let y_offset = 100
    let size_offset = 50
    console.log(filteredData)
    $('.fretboard-note').remove();

    // First Loop: Preload Images
    const preloadPromises = filteredData.map(noteData => {
        return new Promise((resolve, reject) => {
            const preloader = new Image();
            const encodedImagePath = `/static/${encodeURIComponent(noteData.image)}`; // Encode special characters more strictly
            console.log(encodedImagePath)
            preloader.src = encodedImagePath;
    

            preloader.onload = () => {
                console.log(`Image loaded successfully: ${noteData.image}`);
                resolve(noteData); // Resolve with the noteData if loading succeeds
            };

            preloader.onerror = () => {
                console.error(`Failed to load image: ${noteData.image}`);
                reject(new Error(`Failed to load image: ${noteData.image}`)); // Reject on error
            };
        });
    });

        // Run the first loop to preload images
    Promise.all(preloadPromises)
    .then(preloadedData => {
        console.log('All images preloaded successfully.');

        // Second Loop: Update SVG Elements
        preloadedData.forEach(noteData => {
            const { id, image, note, pitch, x, y, string, fret, inversion, string_set } = noteData;

            // Find or create the SVG <image> element
            let noteElement = document.getElementById(id);
            const svgContainer = document.getElementById('guitar-fretboard');

            if (!noteElement) {
                noteElement = document.createElementNS('http://www.w3.org/2000/svg', 'image');
                noteElement.setAttribute('id', id);
                noteElement.classList.add('fretboard-note');
                svgContainer.appendChild(noteElement);
            }

            // Update attributes
            const encodedImagePath = encodeURI(`/static/${image}`);
            noteElement.setAttributeNS('http://www.w3.org/1999/xlink', 'href', encodedImagePath);
            console.log(image,encodedImagePath)
            noteElement.setAttribute('x', x + x_offset - size_offset);
            noteElement.setAttribute('y', y + y_offset - size_offset);
            noteElement.setAttribute('width', '100'); // Set width
            noteElement.setAttribute('height', '100'); // Set height
            noteElement.setAttribute('onclick', `toggleNoteActive('${id}')`);
        });
    })
    .catch(error => {
        console.error('Error loading one or more images:', error);
    });
    /*
    console.log("---------------------------------------");
    console.log(filteredData)
    console.log("---------------------------------------");

    // Clear any existing notes on the fretboard
    //$('.fretboard-note').removeClass('active');
    const svgContainer = document.getElementById('guitar-fretboard');
    console.log("---> befor remove")
    console.log(svgContainer)
    console.log("-------------------------")
    //$('.fretboard-note').remove();
    console.log("---> after remove")
    console.log(svgContainer)
    console.log("-------------------------")
    const elementsToRemove = svgContainer.querySelectorAll('.fretboard-note');
    console.log(elementsToRemove)
    const elementsToRemove2 = document.querySelectorAll('.fretboard-note');
    console.log("Elements found:", elementsToRemove2);
    window.onload = () => {
        console.log("Window fully loaded, running script...");
        
        // Your JavaScript code here
        const elementsToRemove4 = document.querySelectorAll('.fretboard-note');
        console.log("Elements found:", elementsToRemove4);
    
        elementsToRemove4.forEach(el => {
            el.remove();
            console.log("Removed:", el);
        });
    
        // Add more JavaScript logic as needed
    };
    elementsToRemove.forEach(element => element.remove());
    console.log("---> after remove2")
    console.log(svgContainer)
    console.log("-------------------------")

    // Loop through filtered data
    filteredData.forEach(function(noteData) {
        let x_offset = 200
        let y_offset = 100
        let size_offset = 50


        const { id, image, note, pitch, x, y, string, fret, inversion, string_set } = noteData;
        
        
        


        let noteElement = document.getElementById(id);
       
        console.log(noteElement)
        if (!noteElement) {
            noteElement = document.createElement('image');
            noteElement.setAttribute('id', id);
            noteElement.classList.add('fretboard-note');
    
            // Set image attributes
            noteElement.setAttributeNS('http://www.w3.org/1999/xlink', 'href', `/static/${image}`);
            //noteElement.setAttribute('href', `/static/${image}`);

            noteElement.setAttribute('x', x + x_offset - size_offset);
            noteElement.setAttribute('y', y + y_offset - size_offset);
            //noteElement.setAttribute('width', '100');  // Adjust as needed
            //noteElement.setAttribute('height', '100'); // Adjust as needed
            noteElement.style.width = '100px';
            noteElement.style.height = '100px';
            //noteElement.setAttribute('preserveAspectRatio', 'none'); // Optional, may help with rendering

            noteElement.setAttribute('onclick', `toggleNoteActive('${id}')`);
            svgContainer.appendChild(noteElement);

    
            // Add the element to the SVG
            //document.getElementById('guitar-fretboard').appendChild(noteElement);
        }
                
        // Force reflow as a last resort
        svgContainer.style.display = 'none';
        svgContainer.offsetHeight; // Trigger reflow
        svgContainer.style.display = 'block';
        console.log("--->",noteElement)
    });
    console.log(svgContainer)
*/
}

// Initial load: send default configuration on page load
$(document).ready(function() {
    console.log("Page loaded - sending default configuration");
    sendConfiguration(); // This will send the default configuration initially
});

// Send user-selected configuration on button click
$('#applyConfigBtn').on('click', function() {
    console.log("Configuration button clicked - sending selected configuration");
    sendConfiguration(); // Send updated configuration when button is clicked
});
