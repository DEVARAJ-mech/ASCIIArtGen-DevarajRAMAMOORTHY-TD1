from flask import Flask, request, jsonify
import pyfiglet
from flask_cors import CORS

app = Flask(__name__)

# Enable CORS for all routes and origins
CORS(app, resources={r"/*": {"origins": "*"}})



@app.route('/')
def home():
    """Home route providing API information."""
    return "Welcome to the ASCII Art Generator API!"

@app.route('/generate_ascii', methods=['POST'])
def generate_ascii():
    """
    Endpoint to generate ASCII art from input text.
    Expects JSON data with a 'text' field.
    """
    data = request.json
    text = data.get("text", "")
    if not text:
        return jsonify({"error": "Text input is required"}), 400

    try:
        # Generate ASCII art using pyfiglet
       font = data.get("font", "standard")
       ascii_art = pyfiglet.figlet_format(text, font=font)
    except Exception as e:
        # Return error message if ASCII generation fails
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # Start the Flask app in debug mode
    app.run(debug=True)
