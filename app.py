from flask import Flask, render_template, request
from ai_service import fraga_ai
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        problem = request.form.get("problem")
        print(problem)
        answer = fraga_ai(problem)
        return render_template("index.html", problem=problem, answer=answer)
    return render_template("index.html")
