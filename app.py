from flask import Flask, request, render_template, jsonify
from textsummarise import summarize_text  # Import the function from textsummarize.py

def create_app():
    app = Flask(__name__)

    @app.route("/", methods=["GET", "POST"])
    def index():
        if request.method == "POST":
            text = request.form["inputText"]
            print(text)
            max_sentences = float(request.form.get("maxSentences", 0.5))
            print(max_sentences)
            summarized_text = summarize_text(text, max_sentences=max_sentences)
             # Print the summary in the terminal
            print("Summary:")
            print(summarized_text)
            return jsonify({"summary": summarized_text})

        return render_template("index.html")

    return app

if __name__ == "__main__":
    create_app().run(host="127.0.0.1", port=5000, debug=True)
