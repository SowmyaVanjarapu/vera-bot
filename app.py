from flask import Flask, request, jsonify

app = Flask(__name__)

#  Home route (avoids 404)
@app.route('/')
def home():
    return "Vera Bot is Running 🚀"


# Health check
@app.route('/v1/healthz')
def health():
    return "OK"


#  Metadata
@app.route('/v1/metadata')
def metadata():
    return jsonify({
        "name": "Sowmya Bot",
        "version": "1.0"
    })


# Context endpoint
@app.route('/v1/context', methods=['POST'])
def context():
    return jsonify({
        "status": "context received"
    })


#  Tick endpoint
@app.route('/v1/tick', methods=['POST'])
def tick():
    return jsonify({
        "status": "tick processed"
    })


# Reply endpoint (MAIN LOGIC)
@app.route('/v1/reply', methods=['POST'])
def reply():
    # Safe JSON handling (prevents crashes)
    data = request.get_json(silent=True) or {}
    text = data.get("text", "").lower()

    # Category classification logic
    if any(word in text for word in ["swiggy", "zomato", "food", "restaurant"]):
        category = "Food"
    elif any(word in text for word in ["uber", "ola", "cab", "taxi", "ride"]):
        category = "Travel"
    elif any(word in text for word in ["amazon", "flipkart", "shopping", "order"]):
        category = "Shopping"
    else:
        category = "Others"

    return jsonify({
        "category": category
    })


# ✅ Run app (required for Render)
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
