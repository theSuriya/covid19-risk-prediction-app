# COVID-19 Risk Prediction App

Welcome to the COVID-19 Risk Prediction App! This application helps users determine their risk level of contracting COVID-19 based on their personal details.


## Model creation

Before going to build an app frst use the covid-19 classification notebook .ipynb file to train a model just run all the cells and save trained model then upload the model file in the main directory then go through the below steps.


## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [API Documentation](#api-documentation)
- [Technologies Used](#technologies-used)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Introduction
This COVID-19 Risk Prediction App is designed to evaluate a user's risk of contracting COVID-19 based on the provided personal details. The app leverages a FastAPI backend to process the data and predict the risk level.

## Features
- User-friendly web interface to submit personal details.
- Predicts the risk level of COVID-19 infection.
- Fast and efficient API built with FastAPI.
- Clear and concise results displayed to the user.

## Installation
To get a local copy up and running, follow these steps:

### Prerequisites
- Python 3.7+
### Backend Setup
1. Clone the repo:
    ```sh
    git clone https://github.com/your-username/covid19-risk-prediction-app.git
    ```
2. Navigate to the project directory:
    ```sh
    cd covid19-risk-prediction-app
    ```
3. Set up a virtual environment:
    ```sh
    python -m venv env
    ```
4. Activate the virtual environment:
    - On Windows:
      ```sh
      .\env\Scripts\activate
      ```
    - On macOS/Linux:
      ```sh
      source env/bin/activate
      ```
5. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```
6. Run the Main.py File:

## Usage
1. Ensure the FastAPI server is running.
2. Open your web browser and navigate to `http://localhost:3000`.
3. Fill in the required personal details in the form.
4. Submit the form to get the risk prediction result.

## API Documentation
The FastAPI server includes interactive API documentation. Once the server is running, you can access it at:
- Swagger UI: `http://127.0.0.1:8000/docs`
- ReDoc: `http://127.0.0.1:8000/redoc`

## Technologies Used
- **Frontend:** HTML, CSS, JavaScript
- **Backend:** Python, FastAPI
- **Server:** Uvicorn

## Contributing
Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## Contact
Your Name - [thesuriya3@gmail.com](mailto:your-email@example.com)

