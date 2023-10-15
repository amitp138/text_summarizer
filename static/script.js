document.addEventListener("DOMContentLoaded", function() {
    const textForm = document.getElementById("textForm"); // Form element

    textForm.addEventListener("submit", function(event) {
        event.preventDefault(); // Prevent the form from submitting the traditional way

        const inputText = document.getElementById("inputText");
        const summary = document.getElementById("summary");

        const formData = new FormData(textForm); // Create a FormData object from the form

        // Make a POST request to the Flask backend
        fetch("/", {
            method: "POST",
            body: formData,
        })
        .then(response => response.json())
        .then(data => {
            summary.textContent = data.summary; // Display the summary in the UI
        })
        .catch(error => console.error("Error:", error));
    });
});
