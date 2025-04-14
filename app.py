from flask import Flask, render_template, request, jsonify
from retrival import get_answer  # Make sure this function is defined in retrival.py

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json()
    question = data.get("question", "")

    if not question:
        return jsonify({"answer": "Please enter a question.", "source": "N/A"})

    answer, source = get_answer(question)
    return jsonify({"answer": answer, "source": source})


if __name__ == '__main__':
    app.run(debug=True, port=5050)

