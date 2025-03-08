from flask import Flask, render_template, request
import pickle
import re
import nltk
import numpy as np
from nltk.corpus import stopwords

nltk.download('stopwords')

app = Flask(__name__)
with open("model.pkl", "rb") as model_file:
    model = pickle.load(model_file)

with open("vectorizer.pkl", "rb") as vectorizer_file:
    vectorizer = pickle.load(vectorizer_file)
def preprocess_text(text):
    text = re.sub(r'\W', ' ', text)  
    text = text.lower()  
    text = ' '.join([word for word in text.split() if word not in stopwords.words('english')])
    return text
def analyze_text(text):
    words = text.split()
    sentences = re.split(r'[.!?]', text)
    paragraphs = text.split("\n")
    
    word_count = len(words)
    char_count = len(text)
    sentence_count = len([s for s in sentences if len(s.strip()) > 0])
    paragraph_count = len([p for p in paragraphs if len(p.strip()) > 0])
    avg_word_length = round(sum(len(word) for word in words) / word_count, 2) if word_count > 0 else 0
    
    return word_count, char_count, sentence_count, paragraph_count, avg_word_length

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        essay = request.form['essay']
        processed_essay = preprocess_text(essay)
        transformed_essay = vectorizer.transform([processed_essay])
        predicted_score = model.predict(transformed_essay)[0]
        word_count, char_count, sentence_count, paragraph_count, avg_word_length = analyze_text(essay)

        return render_template('result.html', essay=essay, score=round(predicted_score, 2),
                               words=word_count, chars=char_count, 
                               sentences=sentence_count, paragraphs=paragraph_count, 
                               avg_word_length=avg_word_length)

if __name__ == '__main__':
    app.run(debug=True)
