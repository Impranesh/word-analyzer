from flask import Flask, request, jsonify, render_template
import requests
from bs4 import BeautifulSoup
from collections import Counter
import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import string

nltk.download('stopwords')
nltk.download('punkt')
nltk.download('wordnet')

app = Flask(__name__)

# Frontend route (renders the HTML page)
@app.route('/')
def index():
    return render_template('index.html')

# API endpoint for analyzing the website content
@app.route('/api/analyze', methods=['POST'])
def analyze_content():
    data = request.get_json()
    url = data.get('url')
    n = data.get('top_n', 10)

    if not url:
        return jsonify({"error": "URL is required"}), 400

    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')

        # Remove irrelevant content
        for script in soup(["script", "style"]):
            script.extract()

        text = soup.get_text(separator=" ")

        # Clean up the text: Remove punctuation and extra whitespaces
        text = re.sub(r'\s+', ' ', text)
        text = text.translate(str.maketrans('', '', string.punctuation))

        # Tokenize and process text
        words = word_tokenize(text.lower())
        stop_words = set(stopwords.words('english'))
        lemmatizer = WordNetLemmatizer()

        words = [lemmatizer.lemmatize(word) for word in words if word.isalpha() and word not in stop_words]
        word_counts = Counter(words)

        # Get the top N most frequent words
        top_words = word_counts.most_common(n)

        return jsonify({"url": url, "top_words": top_words}),200

    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
