# SRH University Chatbot
A web-based chatbot to assist SRH University Heidelberg students with their inquiries.

## Getting Started

### Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/srh-chatbot.git
cd srh-chatbot


pip install -r requirements.txt

Prerequisites
Python 3.8 or higher
Flask
GPT-2 from Hugging Face's Transformers library
Access to a GPU is recommended for faster processing, but not required.
Setup
Ensure you have the necessary Python environment and dependencies installed. You will need flask and transformers among other packages listed in requirements.txt.

Running the Server Locally
Navigate to the project directory:

Navigate Project Directory:
cd path_to_your_project

Start Flask Server:
python app.py

This will start the local development server on http://127.0.0.1:5000/. You can open this URL in your web browser to interact with the chatbot.

Environment Configuration
Make sure to set up the environment variables correctly if your application requires any. This includes any API keys or specific configurations needed for deployment.

Usage
Interact with the chatbot through the web interface provided by Flask. The chatbot is capable of answering queries related to SRH University Heidelberg, such as registration deadlines, contact information, and course details.

Features
Natural Language Understanding: The chatbot uses GPT-2 to understand and generate human-like responses.
Flask Web Server: Serves the chatbot interface and handles user requests.
Responsive Design: The interface is designed to work on both desktop and mobile browsers.

Future Enhancements
Implement additional NLP features such as sentiment analysis.
Integrate with university databases for real-time information updates.
Provide multilingual support to assist international students.

License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgments
Thanks to SRH University Heidelberg for providing the initial data and requirements for the chatbot.
Thanks to the Hugging Face team for providing the transformers library which powers the underlying NLP model.


This README file provides a comprehensive guide to setting up and running your Flask-based chatbot application, along with details on how to use it and future enhancement possibilities. Adjust paths, URLs, and any specific steps according to your actual setup and hosting details.
