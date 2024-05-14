Github Link - https://github.com/ashwith1/mini.git

SRH-University-Chatbot
    A web-based chatbot to assist SRH University Heidelberg students with their inquiries.

Getting Started-

1. Clone the repository:
    git clone https://github.com/ashwith1/mini.git


2. Installation:
    pip install -r requirements.txt

3. Prerequisites:
    Python 3.8 or higher
    Flask
    GPT-2 from Hugging Face's Transformers library
    Access to a GPU is recommended for faster processing, but not required.
    
4. Setup
    Ensure you have the necessary Python environment and dependencies installed. You will need flask and transformers among other packages listed in requirements.txt.

    Start Flask Server:
    python app.py

5. Running the Server Locally:
    Navigate to the project directory

This will start the local development server on http://127.0.0.1:5000/. You can open this URL in your web browser to interact with the chatbot.


7. Environment Configuration:
    Make sure to set up the environment variables correctly if your application requires any. 
    This includes any specific configurations needed for deployment.

8. Usage:
    Interact with the chatbot through the web interface provided by Flask. 
    The chatbot is capable of answering queries related to SRH University Heidelberg, such as registration deadlines, contact information, and course details.

9. Features:
    Natural Language Understanding: The chatbot uses GPT-2 to understand and generate human-like responses.
    Flask Web Server: Serves the chatbot interface and handles user requests.
    Responsive Design: The interface is designed to work on both desktop and mobile browsers.

10. Future Enhancements:
    Add better datasets to improve the reliability and accuracy of the model.
    Improve the web interface to enhance user experience.
    Implement additional NLP features such as sentiment analysis.
    Integrate with university databases for real-time information updates.
    Provide multilingual support to assist international students.


Acknowledgments-
    Thanks to SRH University Heidelberg for providing the initial data and requirements for the chatbot.
    Thanks to the Hugging Face team for providing the transformers library which powers the underlying NLP model.
