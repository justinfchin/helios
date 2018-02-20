from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    # result = None
    if request.method == "POST":
        result = request.form["inputText"]
        return render_template("index.html", result=result)  # pass param
    return render_template("index.html", result=None)


if __name__ == '__main__':
    app.run()
