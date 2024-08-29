# Content Check
Watch the demo video here: [Demo Video](https:(https://drive.google.com/file/d/1mwT8Y6hl34EnB9v8ksdULaE4uLAKm4x2/view?usp=sharing))
## Overview

**Content Check** is a web application that allows users to paste text and generate a similarity report by comparing the input text against content found on the web. The application utilizes Flask for the backend and provides a user-friendly interface for text input and report generation.

## Features

- **Text Input**: Paste your text into a text area for analysis.
- **Similarity Report**: Generates a report showing the similarity of your text with content found on the web.
- **Responsive Design**: The application is designed to be user-friendly on both desktop and mobile devices.

## Project Structure

- `index.html`: The main HTML file for the text input form.
- `report.html`: The HTML template for displaying the similarity report.
- `app.py`: The main Flask application file.
- `report.py`: Contains the logic for text similarity checking and web search.
- `websearch.py`: Handles web searches and text extraction from URLs.
- `static/`: Contains static files such as images and CSS.
- `templates/`: Contains HTML templates for Flask.



## Technologies Used

- **Flask**: A lightweight WSGI web application framework for Python, used for the backend server.
- **NLTK (Natural Language Toolkit)**: A library for working with human language data (text), used for text processing and analysis.
- **Requests**: A Python library for making HTTP requests, used for fetching web content.
- **BeautifulSoup**: A library for parsing HTML and XML documents, used for extracting text from web pages.
- **Pandas**: A data manipulation and analysis library, used for creating and managing the similarity report table.

## Libraries

- **Flask**: `flask` (Web framework)
- **NLTK**: `nltk` (Natural language processing)
- **Requests**: `requests` (HTTP requests)
- **BeautifulSoup**: `beautifulsoup4` (HTML parsing)
- **Pandas**: `pandas` (Data handling)

## How It Works

1. **Text Processing**:
   - The input text is processed to remove stopwords and tokenize it into sentences.
   - This purified text is then used to search for similar content on the web.

2. **Web Search**:
   - The application uses Bing search through `websearch.py` to find relevant web pages containing the input text or related sentences.
   - Up to 10 matching URLs are retrieved for analysis.

3. **Text Extraction and Similarity Calculation**:
   - The text content from the retrieved URLs is extracted using BeautifulSoup.
   - The similarity between the input text and the content from each URL is calculated using the `SequenceMatcher` from Python's `difflib` module.

4. **Report Generation**:
   - A similarity report is generated and formatted into an HTML table using Pandas.
   - The report displays the source URLs and their similarity percentages, providing clickable links to the original content.

## Setup and Installation

### Prerequisites

- Python 3.6 or higher
- pip (Python package installer)

### Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/sujayv16/content-check.git
   cd content-check

2. **Create and Activate a Virtual Environment**

   python -m venv venv

    

3. **Install Requirements**
    ```bash
   pip install -r requirements.txt

4. **Download NLTK Data**
    ```bash
   python -c "import nltk; nltk.download('stopwords'); nltk.download('punkt')"

## Running the Application

   Start the Flask development server:
    ```bash
   python app.py

Open your browser and go to http://localhost:5555 to use the application.
