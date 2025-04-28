from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Simple chatbot logic
def get_bot_response(user_input):
    user_input = user_input.lower()
    if "billing" in user_input:
        return "For billing issues, please check your invoice or contact billing@yourcompany.com."
    elif "technical" in user_input:
        return "For technical support, please reboot your device and try again."
    elif "refund" in user_input:
        return "Refunds are processed within 5-7 business days."
    elif "hello" in user_input or "hi" in user_input:
        return "Hello! How can I assist you today?"
    else:
        return "I'm sorry, I didn't understand that. Please type 'billing', 'technical', or 'refund'."

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get", methods=["POST"])
def chatbot_response():
    user_input = request.form["msg"]
    bot_response = get_bot_response(user_input)
    return jsonify({"response": bot_response})

if __name__ == "__main__":
    app.run(debug=True)
