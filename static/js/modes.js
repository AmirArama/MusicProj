document.addEventListener("DOMContentLoaded", function () {
    const keyDropdown = document.getElementById("keyDropdown");
    const viewDropdown = document.getElementById("ViewDropdown");
    const circleImage = document.querySelector("#circle_of_fifths_modes image");

    // Function to update the image href based on dropdown selections
    function updateImage() {
        const selectedKey = keyDropdown.value; // Get selected key
        const selectedView = viewDropdown.value; // Get selected view
        // Construct the new image path
        const newImagePath = `/static/images/circle/circle_of_fifths_${selectedKey.toLowerCase()}_${selectedView.toLowerCase()}.png`;
        console.log(newImagePath)

        // Update the image href
        circleImage.setAttribute("href", newImagePath);
    }

    // Add event listeners to both dropdowns
    keyDropdown.addEventListener("change", updateImage);
    viewDropdown.addEventListener("change", updateImage);

    // Initialize the image on page load
    updateImage();
});

document.addEventListener("DOMContentLoaded", function () {
    const carousel = document.querySelector('#theoryCarousel');
    const prevButton = document.querySelector('.carousel-control-prev');
    const nextButton = document.querySelector('.carousel-control-next');

    prevButton.addEventListener('click', function (event) {
        event.preventDefault(); // Prevent default button action
        new bootstrap.Carousel(carousel).prev(); // Move to the previous slide
    });

    nextButton.addEventListener('click', function (event) {
        event.preventDefault(); // Prevent default button action
        new bootstrap.Carousel(carousel).next(); // Move to the next slide
    });
});
