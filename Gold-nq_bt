from flask import Flask, request
app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    print(f"Signal received: {data}")
    return "ok", 200

@app.route('/')
def home():
    return "Gold NQ Bot is running!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
