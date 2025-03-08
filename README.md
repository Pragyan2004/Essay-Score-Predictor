## Essay Score Predictor

# Overview
The Essay Score Predictor is a Flask-based web application that predicts the quality score of an essay using a trained Machine Learning model. The system preprocesses user input, extracts key text features, and then uses a pre-trained model to generate a score.

# Features
✔️ Real-time Word & Character Count
✔️ Text File Upload Support
✔️ Pre-Trained ML Model for Prediction
✔️ Text Analytics (Word Count, Sentences, Paragraphs, Avg. Word Length)

# Run the Flask app

    python app.py

Open your browser and visit http://127.0.0.1:5000/

# Backend (Flask) – app.py
Loads a pre-trained ML model (model.pkl) and a vectorizer (vectorizer.pkl).
Preprocesses text by removing stopwords and special characters.
Extracts text features (word count, sentence count, etc.).
Predicts an essay score using the ML model.
Displays results on result.html.

# Frontend (HTML, CSS, JS)
index.html: UI for essay input and file upload.
script.js: Real-time word & character count updates.
style.css: Responsive design and styling.

# Usage
Paste or upload an essay
Click "Predict Score"
View detailed analysis & score

# Screenshot
![Screenshot 2025-03-08 231431](https://github.com/user-attachments/assets/b9d2856e-b1c1-4310-87fa-257f6ba6765e)

![Screenshot 2025-03-08 231443](https://github.com/user-attachments/assets/c7f71ee2-02e9-46be-86a7-4562c8e817fe)

