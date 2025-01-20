# ASCIIArtGen-DevarajRAMAMOORTHY-TD1
The project contains the code for the application that can display the text to ASCII art form
3D ASCII Art Generator
The 3D ASCII Art Generator is a web application that allows users to convert input text into ASCII art and visualize it in 3D. This project includes a Python backend (Flask) and a JavaScript-based frontend, offering an interactive experience for generating and exploring ASCII art in a creative way.

Features
Generate ASCII Art: Converts user input text into ASCII art using the pyfiglet library.
3D Visualization: Displays the ASCII art in a 3D format using Plotly.js.
Font Selection: Allows users to select different ASCII art fonts (optional feature).
Download ASCII Art: Enables downloading the generated ASCII art as a .txt file.
Simple and Interactive UI: A clean and intuitive interface to make the process easy for users.
Technologies Used
Backend:
Flask: Python web framework to handle requests and process ASCII art generation.
pyfiglet: Python library for creating ASCII art from text.
Flask-CORS: To handle cross-origin requests between frontend and backend.
Frontend:
HTML/CSS: For the web interface.
JavaScript: For user interactions and communicating with the backend.
Plotly.js: For rendering 3D visualizations of the ASCII art.
Installation
Prerequisites:
Python 3.7 or later
A web browser (Google Chrome, Mozilla Firefox, etc.)
Node.js (optional for advanced customizations)
Steps to Set Up the Project:
Clone the Repository:

bash
Copy
Edit
git clone <repository_url>
cd 3D-ASCII-Art-Generator
Set Up the Virtual Environment:

bash
Copy
Edit
python -m venv venv
source venv/bin/activate   # On Linux/Mac
venv\Scripts\activate      # On Windows
Install Dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Run the Backend:

bash
Copy
Edit
cd backend
python app.py
The backend server will start running on http://127.0.0.1:5000.

Open the Frontend: Open the index.html file in your browser.

Usage
Enter the text you want to convert into ASCII art.
Click the "Generate 3D ASCII Art" button.
View the ASCII art and its 3D visualization.
Use the "Download ASCII Art" button to save the generated art as a .txt file.
Project Structure
php
Copy
Edit
3D-ASCII-Art-Generator/
├── backend/
│   ├── app.py               # Flask backend
│   ├── requirements.txt     # Backend dependencies
├── index.html               # Frontend interface
├── README.md                # Project documentation
Future Improvements
Font Selection: Allow users to choose from multiple ASCII art fonts.
Color Customization: Enable users to set custom colors for 3D visualization.
Save as Image: Add an option to save ASCII art as an image file (e.g., PNG, JPEG).
Contributing
Contributions are welcome! Please follow these steps to contribute:

Fork the repository.
Create a new branch for your feature or bug fix.
Submit a pull request with a detailed description of your changes.
License
This project is licensed under the MIT License. See the LICENSE file for more details.

Acknowledgments
pyfiglet: For providing easy-to-use ASCII art generation.
Plotly.js: For creating stunning 3D visualizations.
Enjoy using the 3D ASCII Art Generator! 🎨✨
