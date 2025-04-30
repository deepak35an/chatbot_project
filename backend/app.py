from flask import Flask, render_template, request, jsonify
import pickle

app = Flask(__name__, static_folder='static')

# Load the trained intent classifier model
with open("intent_model.pkl", "rb") as f:
    intent_model = pickle.load(f)

# Predefined responses for each intent
responses = {
    "billing": "For billing issues, please check your invoice or contact billing@yourcompany.com.",
    "technical": "For technical support, please reboot your device and try again. If the issue persists, contact support@yourcompany.com.",
    "refund": "Refunds are processed within 5-7 business days. If you need assistance with a refund, contact refunds@yourcompany.com.",
    "account": "For account issues such as login or password reset, please use the 'Forgot Password' link or contact account@yourcompany.com.",
    "greeting": "Hello! How can I assist you today?"
}

# Fallback for unknown intent
default_response = "I'm sorry, I didn't understand that. Please type a question about billing, technical issues, refunds, or account help."

# Chatbot response logic using the ML model
def get_bot_response(user_input):
    try:
        # Predict the intent using the trained model
        predicted_intent = intent_model.predict([user_input])[0]
        return responses.get(predicted_intent, default_response)
    except Exception as e:
        print(f"Error: {e}")
        return default_response

@app.route("/")
def home():
    return render_template("index.html")  # Your chat UI HTML file

@app.route("/get", methods=["POST"])
def chatbot_response():
    user_input = request.form["msg"]  # Get user message from JS
    bot_response = get_bot_response(user_input)  # Get model-based reply
    return jsonify({"response": bot_response})  # Return JSON

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
