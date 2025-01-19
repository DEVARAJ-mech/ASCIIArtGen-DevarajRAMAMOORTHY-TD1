from flask import Flask, request, jsonify
import pyfiglet
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return "Welcome to the ASCII Art Generator API!"


@app.route('/generate_ascii', methods=['POST'])
def generate_ascii():
    data = request.json
    text = data.get("text", "")
    if not text:
        return jsonify({"error": "Text input is required"}), 400

    try:
        ascii_art = pyfiglet.figlet_format(text)
        return jsonify({"ascii_art": ascii_art})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
