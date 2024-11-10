# Word Frequency Analyzer

This is a web application that analyzes the frequency of words from a webpage. The application consists of a Flask-based REST API as the backend and a simple HTML frontend that interacts with the API. It fetches a webpage, processes the content to remove stopwords, and returns the most frequent words in that content.

## Features
- Input any URL and specify how many top words you want to analyze.
- The Flask REST API fetches and processes the webpage content.
- Displays the most frequent words and their frequencies in a table.

## Technologies Used
- **Backend**: Flask, BeautifulSoup, NLTK (Natural Language Toolkit), Python 3
- **Frontend**: HTML, CSS (optional), JavaScript (Fetch API)

---

## Setup Instructions

### Prerequisites

Make sure you have the following installed on your machine:
- Python 3.x
- `pip` (Python package manager)

### Step 1: Clone the repository

```bash
git clone <your-repo-url>
cd word-analyzer
```

### Step 2: Set up a virtual environment (Optional but recommended)


Create and activate a Python virtual environment:

On macOS/Linux:
```bash

python3 -m venv venv
source venv/bin/activate
```

On Windows:
```bash

python -m venv venv
venv\Scripts\activate
```
### Step 3: Install dependencies
Install the required Python packages:
```bash
pip install -r requirements.txt

```
Or manually install the dependencies:
```bash
pip install flask requests beautifulsoup4 nltk

```
### Step 4: Download NLTK data
You will need to download some NLTK corpora for tokenizing and processing text. Open a Python shell and run:
```bash
import nltk
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('wordnet')
```
### Step 5: Run the application
Once everything is set up, you can start the Flask development server:
```bash
python app.py

```
This will start the server at http://127.0.0.1:5000/.
### Project Structure
word-analyzer/

- **`app.py`**: This is the main file for the Flask backend. It handles both the API routes and the rendering of the frontend pages.
  
- **`requirements.txt`**: This file lists all the Python dependencies required to run the project. You can install them using `pip install -r requirements.txt`.

- **`static/`**: This directory contains static assets like CSS and JavaScript files. For this project, it contains the `style.css` file to style the frontend page.

- **`templates/`**: This directory contains HTML templates. In this project, it includes the `index.html` file, which is used for the frontend user interface.

- **`README.md`**: This file provides an overview of the project, installation instructions, and API documentation.

### API Documentation

The backend exposes a REST API endpoint at /api/analyze for analyzing webpage content.

## Endpoint: /api/analyze
-**`Method`**: POST

-**`Description`**: Analyzes the word frequency of the content from the provided webpage URL.

-**`Request Body (JSON)`**:
```bash
{
  "url": "https://example.com",   // The webpage URL to analyze
  "top_n": 10                     // (Optional) The number of top words to return (default is 10)
}

```
-**`Response (JSON)`**:
```bash
{
  "url": "https://example.com",
  "top_words": [
    ["word1", 12],
    ["word2", 8],
    ["word3", 5]
  ]
}

```
-**`Error Response`**:
```bash
{
  "error": "Invalid URL"
}

```
-**`Example curl Request`**:
```bash
curl -X POST http://127.0.0.1:5000/api/analyze \
-H "Content-Type: application/json" \
-d '{"url": "https://example.com", "top_n": 5}'

```
## Frontend Details :
The frontend is a simple HTML page that allows users to input:

- The URL of the website to analyze.
- The number of top words to display.
  
 After submitting the form, the frontend sends a request to the API and dynamically displays the word frequency results in a table using JavaScript's Fetch API.
## How It Works
-**`Frontend`**: The user submits a URL and the desired number of top words through an HTML form.

-**`Backend`**: The Flask backend fetches the webpage, processes the content using NLTK (Natural Language Toolkit) and BeautifulSoup, and returns the top N most frequent words.

-**`Results`**: The frontend displays the results in a table without reloading the page.

## Troubleshooting
- Common Issues:
  
**`TemplateNotFound Error`**: Ensure that your index.html file is located inside the templates directory.

**`500 Internal Server Error`**: This might happen if the webpage cannot be fetched. Check if the provided URL is valid and accessible.

**`CORS Error`**: If you are accessing the API from a different domain, make sure to handle CORS in your Flask app by using the flask-cors library.

## Note :

You can further customize the frontend by editing the index.html and style.css files in the templates and static directories, respectively.
