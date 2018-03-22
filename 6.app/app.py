from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = os.path.abspath(os.curdir) + '/upload'


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        result = request.form["inputText"]
        return render_template("index.html", result=result)  # pass param
    return render_template("index.html", result=None)


@app.route('/uploader', methods=['POST'])
def uploader():
    f = request.files['file']
    f.save(os.path.join(app.config['UPLOAD_FOLDER'],
                        secure_filename(f.filename)))
    return "File uploaded successfully"


if __name__ == '__main__':
    app.run()
