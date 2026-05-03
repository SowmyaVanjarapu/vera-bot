from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/v1/healthz')
def health():
    return "OK"

@app.route('/v1/metadata')
def metadata():
    return jsonify({"name": "Sowmya Bot", "version": "1.0"})

@app.route('/v1/context', methods=['POST'])
def context():
    return jsonify({"status": "context received"})

@app.route('/v1/tick', methods=['POST'])
def tick():
    return jsonify({"status": "tick processed"})

@app.route('/v1/reply', methods=['POST'])
def reply():
    data = request.json
    text = data.get("text", "").lower()

    if "swiggy" in text or "zomato" in text:
        category = "Food"
    elif "uber" in text or "ola" in text:
        category = "Travel"
    elif "amazon" in text:
        category = "Shopping"
    else:
        category = "Others"

    return jsonify({"category": category})