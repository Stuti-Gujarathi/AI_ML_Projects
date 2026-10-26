"""Flask web UI for the AIML chatbot. Run: python app.py  ->  http://127.0.0.1:5000"""
import uuid
from flask import Flask, jsonify, render_template, request, session
from bot import create_bot, reply

app = Flask(__name__)
app.secret_key = "change-this-secret-key"
kernel = create_bot()


@app.route("/")
def index():
    session.setdefault("sid", str(uuid.uuid4()))
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():
    sid = session.setdefault("sid", str(uuid.uuid4()))
    message = (request.get_json(silent=True) or {}).get("message", "").strip()
    if not message:
        return jsonify({"reply": "Please type something."})
    return jsonify({"reply": reply(kernel, message, sid)})


if __name__ == "__main__":
    app.run(debug=True)
