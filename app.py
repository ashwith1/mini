from flask import Flask, render_template, request, jsonify
from model_utils import load_model, generate_response  # Ensure this import is correct

app = Flask(__name__, template_folder='templates')  # Make sure your templates folder has the correct HTML files

# Load model and tokenizer from the correct directory
model_directory = r'C:\\Users\\asha4\\OneDrive\\Desktop\\mini\\mini'  # Update this path to your model directory
model, tokenizer = load_model(model_directory)

@app.route('/')
def home():
    return render_template('index.html')  # Ensure 'index.html' exists in your templates directory

@app.route('/get', methods=['GET', 'POST'])
def get_bot_response():
    userText = request.values.get('msg')  # Compatible with both GET and POST
    if not userText:
        return jsonify("Please type something to get a response.")
    response = generate_response(tokenizer, model, userText)  # Use your response generation logic
    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True, port=5000)
