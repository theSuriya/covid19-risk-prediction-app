async function predict() {
    const formData = new FormData(document.getElementById("predictionForm"));
    const data = {};
    formData.forEach((value, key) => {
        data[key] = value;
    });

    // Check if any of the fields are empty
    if (!validateFormData(data)) {
        alert('Please fill in all the details before predicting.');
        return;
    }

    try {
        const response = await fetch('/predict', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(data),
        });

        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }

        const result = await response.json();

        // Display the specific information you want
        document.getElementById("predictionResult").innerHTML = `<p>Prediction: ${result.prediction}</p>`;
    } catch (error) {
        console.error('Error:', error);
    }
}

function validateFormData(data) {
    // Check if any of the values are empty or undefined
    for (const key in data) {
        if (data[key] === '' || data[key] === undefined || data[key] === null) {
            return false;
        }
    }
    return true;
}
