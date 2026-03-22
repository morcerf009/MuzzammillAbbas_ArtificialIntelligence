# Customer Support Chatbot

A simple, lightweight, rule-based chatbot built using Python, Flask, HTML, CSS, and JavaScript. This web application interacts with users and provides automated responses to common customer support queries such as pricing, services, working hours, and contact details.

## Project Structure
- `app.py`: The main Flask backend script handling the web server routes and basic chatbot logic via Python's regular expressions.
- `templates/index.html`: The frontend user interface providing an interactive chat window using asynchronous JavaScript UI updates.
- `requirements.txt`: Python package dependencies for the project.

## Features
- **Instant Responses:** Automatically detects keywords and intents to provide immediate answers.
- **Support Queries:** Currently detects Greetings, Services, Pricing, Jobs/Internships, Business Hours, and Contact inquiries.
- **Typing Indicator:** Simulates a user-friendly bot experience using a typing delay.

## Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd "AI Chatbot for Customer Support"
   ```

2. **Install the dependencies:**
   Make sure you have Python installed.
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Flask application:**
   ```bash
   python app.py
   ```

4. **Access the Web Interface:**
   Open a browser and navigate to `http://127.0.0.1:5000` to start chatting.

## Note
Please ensure you update the placeholders in `app.py` for email, phone number, and location context to match your actual business details before deploying.
