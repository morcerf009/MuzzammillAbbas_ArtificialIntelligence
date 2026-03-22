from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

import re

def chatbot_response(user_input):
    user_input = user_input.lower()

    # Greetings
    if re.search(r'\b(hello|hi|hey)\b', user_input):
        return "Hello! 👋 Welcome to our support. How can I assist you today?"

    # Services
    elif re.search(r'\b(services|service)\b', user_input):
        return "We provide AI solutions, web development, and digital marketing services."

    # Pricing
    elif re.search(r'\b(price|cost|charges|pricing)\b', user_input):
        return "Our pricing depends on your requirements. Please share your needs for a quote."

    # Contact
    elif re.search(r'\b(contact|email|phone)\b', user_input):
        return "You can contact us at [Your Email Here] or call [Your Phone Number Here]."

    # Working hours
    elif re.search(r'\b(hours|timing|open)\b', user_input):
        return "We are open from 9 AM to 6 PM, Monday to Friday."

    # Help
    elif re.search(r'\b(help)\b', user_input):
        return "I can help you with services, pricing, contact info, and general queries."

    # Location
    elif re.search(r'\b(location|address)\b', user_input):
        return "We are located in Karachi, Pakistan."

    # Internship / jobs
    elif re.search(r'\b(internship|job|career|jobs|careers)\b', user_input):
        return "We offer internship opportunities. Please send your resume via email."

    # Thanks
    elif re.search(r'\b(thanks|thank you)\b', user_input):
        return "You're welcome! 😊"

    # Goodbye
    elif re.search(r'\b(bye|goodbye)\b', user_input):
        return "Goodbye! 👋 Have a great day!"

    # Default
    else:
        return "I'm not sure I understand. Can you please rephrase your question?"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get", methods=["POST"])
def get_bot_response():
    user_text = request.form["msg"]
    return chatbot_response(user_text)

if __name__ == "__main__":
    app.run(debug=True)