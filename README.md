# Temp_Trend

This project aims to predict the average temperature based on various factors such as food transport, household consumption, retail, packaging, processing, IPPU, fires in organic soils, fires in humid tropical forests, and total emissions and many more. The project uses a machine learning model to make predictions and presents the results in an informative and visually appealing web application.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Model Training](#model-training)
- [Web Application](#web-application)
- [Contributing](#contributing)

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/climate-temperature-prediction.git
    cd climate-temperature-prediction
    ```

2. Create a virtual environment and activate it:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

4. Ensure you have the dataset and model files in the appropriate directories:
    - `path_to_your_dataset.csv`
    - `temperature_model.pkl`

## Usage

1. Run the Flask application:
    ```sh
    python main.py
    ```

2. Open your web browser and go to `http://127.0.0.1:5000/` to access the home page.

3. Navigate through the web application:
    - **Home**: Introduction and project overview.
    - **Prediction**: Input the necessary factors to predict the average temperature.
    - **Data**: View the dataset sample for India.
    - **Solution**: Learn about actions and solutions to mitigate climate change.



## Model Training

The model was trained using historical climate data and various factors influencing temperature changes. The training process involved:

1. **Data Collection**: Gathering data on factors such as food transport, household consumption, retail, packaging, processing, IPPU, fires in organic soils, fires in humid tropical forests, and total emissions.
2. **Data Preprocessing**: Cleaning and preparing the data for training.
3. **Model Selection**: Choosing an appropriate machine learning algorithm (e.g., Linear Regression).
4. **Model Training**: Training the model using the prepared dataset.
5. **Model Evaluation**: Assessing the model's performance using metrics like mean squared error.

The trained model is saved as `model.pkl` and used in the web application to make predictions.

## Web Application

The web application is built using Flask and provides an interactive interface for users to predict average temperatures based on various input factors. The application consists of the following pages:

- **Home**: Overview of the project.
- **Prediction**: Form to input factors and get the temperature prediction.
- **Data**: Display a sample of the dataset filtered for India.
- **Solution**: Provide actionable tips and solutions to mitigate climate change.

## Contributing

Contributions are welcome! If you'd like to contribute, please fork the repository and use a feature branch. Pull requests are warmly welcome.

1. Fork the repository.
2. Create a feature branch: `git checkout -b feature-branch`
3. Commit your changes: `git commit -m 'Add some feature'`
4. Push to the branch: `git push origin feature-branch`
5. Submit a pull request.


