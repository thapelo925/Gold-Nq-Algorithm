 from flask import Flask, request
import requests

app = Flask(__name__)

# === PASTE YOUR VALUES HERE ===
ACCESS_TOKEN = "EAAbR7GaFh6YBS6LccdXXYURRG5QZBJyC7xhLka9879Ox9ju0fc0h7J8GzT7KBI2wZACCmd2CAweIYkj9TPGLBr5f7E6DGXsj93IwwpS7DMtgXmTxRs7gTqO2Kts4ZCpMyoUzlay22IGWjAejJN4ivINQZBGE221vZBZBQBdpDTbiZCw3gfPWo8bQ4Qcnb2MtH5vvdgvWU6ZCtsz4WmSQpdQCP92pT4GCvGkcDcPHRuFd8MeQvZAxscn9JqLfHi3kiUDcjWXsDHZAyhXaCJQw8hh3aSzRKq"  # The long EAA... token
PHONE_NUMBER_ID = "1414440595084120"  # From your screenshot
RECIPIENT_NUMBER = "273466932"  # Your WhatsApp number, e.g. 27821234567
# ==============================

@app.route('/webhook', methods=['POST'])
def webhook():
    try:
        d = request.json
        print(f"Received: {d}")
        
        symbol = d.get('symbol', 'GOLD/NQ')
        direction = d.get('dir', 'BUY/SELL')
        entry = d.get('entry', '')
        sl = d.get('sl', '')
        tp = d.get('tp', '')

        msg = f"🚨 {symbol} M1 SIGNAL\nDir: {direction}\nEntry: {entry}\nSL: {sl}\nTP: {tp}\nRR 1:2.2 Gold/NQ Algo"

        url = f"https://graph.facebook.com/v20.0/{PHONE_NUMBER_ID}/messages"
        headers = {
            "Authorization": f"Bearer {ACCESS_TOKEN}",
            "Content-Type": "application/json"
        }
        payload = {
            "messaging_product": "whatsapp",
            "to": RECIPIENT_NUMBER,
            "type": "text",
            "text": {"body": msg}
        }

        r = requests.post(url, headers=headers, json=payload)
        print(f"WhatsApp Response: {r.text}")
        return f"ok {r.text}", 200

    except Exception as e:
        print(f"Error: {e}")
        return f"error {e}", 500

@app.route('/')
def home():
    return "WhatsApp Gold-NQ Bot OK - /webhook is ready"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
