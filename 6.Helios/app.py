from flask import Flask, render_template, request, session, flash, redirect, url_for
from werkzeug.utils import secure_filename
import os
import filters as fi # for the filters PhotonRave wrote

UPLOAD_FOLDER = os.path.abspath(os.curdir) + '/static/uploads'
ALLOWED_EXTENSIONS =['wav', 'mp3']

app = Flask(__name__)
app.secret_key = "YouWillNeverGuessTheSecretKey"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/', methods=['GET'])
def index():
    return render_template("index.html", audio_link=session.get('uploaded_file'))


@app.route('/uploader', methods=['POST'])
def uploader():
    if 'file' not in request.files:
        flash("There is no file part in the request")
        return redirect(url_for('index'))

    file = request.files['file']

    if file.filename == '':
        flash("No file has been selected")
        return redirect(url_for('index'))

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'],
                               filename))

        session['uploaded_file'] = "/static/uploads/" + filename

        flash('File uploaded successfully')
        return redirect(url_for('index'))

    flash('You tried to upload unsupported file')
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run()
