from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import os
import filters as fi # for the filters PhotonRave wrote

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = os.path.abspath(os.curdir) + '/upload'


# Renders the Homepage 
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        result = request.form["inputText"]
        return render_template("index.html", result=result)  # pass param
    return render_template("index.html", result=None)


# Saves the File in the same directory as app.py & Uploads to Audio
@app.route('/uploader', methods=['POST'])
def uploader():
    f = request.files['file']
    f.save(secure_filename(f.filename))#os.path.join(app.config['UPLOAD_FOLDER'],
                       # secure_filename(f.filename)))
    return render_template("index.html", result="File uploaded successfully")

# Runs the Wiener Filter on the Audio File


if __name__ == '__main__':
    app.run()
