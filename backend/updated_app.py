from flask import Flask, render_template, request, jsonify

app = Flask(__name__, static_folder='static')  # 'static' is default, but included for clarity

# Simple chatbot logic (you can expand this later)
def get_bot_response(user_input):
    user_input = user_input.lower()
    
    if "billing" in user_input:
        return "For billing issues, please check your invoice or contact billing@yourcompany.com."
    elif "technical" in user_input:
        return "For technical support, please reboot your device and try again. If the issue persists, contact support@yourcompany.com."
    elif "refund" in user_input:
        return "Refunds are processed within 5-7 business days. If you need assistance with a refund, contact refunds@yourcompany.com."
    elif "hello" in user_input or "hi" in user_input:
        return "Hello! How can I assist you today?"
    elif "hours" in user_input:
        return "Our office hours are 9 AM to 5 PM, Monday to Friday."
    elif "thank you" in user_input or "thanks" in user_input:
        return "You're welcome! Let me know if you need anything else."
    elif "bye" in user_input or "goodbye" in user_input:
        return "Goodbye! Have a great day!"
    elif "help" in user_input:
        return "I'm here to assist you with billing, technical issues, and refunds. Just type your query!"
    else:
        return "I'm sorry, I didn't understand that. Please type 'billing', 'technical', 'refund', or 'help' for assistance."

@app.route("/")
def home():
    return render_template("index.html")  # Loads from /templates/index.html

@app.route("/get", methods=["POST"])
def chatbot_response():
    user_input = request.form["msg"]  # Get the message sent by JS
    bot_response = get_bot_response(user_input)  # Get the reply from our logic
    return jsonify({"response": bot_response})  # Return as JSON

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
