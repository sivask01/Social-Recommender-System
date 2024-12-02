# Advanced Social Recommendation System

This project implements an advanced recommendation system that integrates time-aware collaborative filtering, sentiment analysis, graph-based analysis, and a hybrid model for more accurate and personalized item recommendations.

## Setup Instructions

### Prerequisites
- Python 3.x
- Required Python libraries are listed in the `requirements.txt` file.

### Installation Steps

1. Clone the repository to your local machine:

git clone <https://github.com/sivask01/Social-Recommender-System>

cd <project_directory>

2. Navigate to the project directory:

python3 -m venv venv
3. Create a virtual environment:

4. Activate the virtual environment:
- For **Windows**:
  ```
  venv\Scripts\activate
  ```
- For **macOS/Linux**:
  ```
  source venv/bin/activate
  ```

5. Install the required dependencies:
6. pip install -r requirements.txt


6. Run the application:
python main.py


The UI will be available at `http://127.0.0.1:5000/`.

## Training Files

All training files are stored in the `Files` folder. These files include:
- jupyter notebooks which inlcudes model training.
- **Saved-Models**: Models are trained and saved in .pkl format in Saved-models folder.

Please ensure that the `Files` folder is intact when running the system, as it contains the necessary files for loading and processing data.

## Usage
Once the app is running, you can interact with the recommendation system by selecting different models and receiving personalized item recommendations based on your preferences.
You can explore different sections of the application, including "Recommendations" for model selection and "Analysis" for insights.


# Deployment

The project has been successfully deployed on Streamlit Cloud, and the application is live. 

### Accessing the Deployed Application
- **Link to Deployed Application**: social-recommender-system-sk.streamlit.app

The deployed version offers the same functionality as the local version, with users able to interact with the recommendation system through the UI and get real-time personalized item recommendations.

## Acknowledgements

- Thank you to all contributors and resources that made this project possible.
- This project was developed as part of Course project CMPE-256(Advanced Data Mining) and a personal learning initiative to enhance skills in building scalable recommendation systems.



