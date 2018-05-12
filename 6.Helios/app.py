from flask import Flask, render_template, request, session, flash, redirect, url_for
from werkzeug.utils import secure_filename
import os
import filters as fi    # for the filters PhotonRave wrote


FILTER_FUNCTIONS = {'Chebyshev I': fi.cheby1, 'Butter': fi.butter, 'Wiener': fi.wiener, 'Butter-Chebyshev': fi.butter_cheby,'Chebyshev-Butter': fi.cheby_butter} 
UPLOAD_FOLDER = os.path.abspath(os.curdir) + '/static/uploads/'
OUTPUT_FOLDER = os.path.abspath(os.curdir) + '/static/results/'
SPEAKER_FOLDER = os.path.abspath(os.curdir) + '/static/speakers/'
ALLOWED_EXTENSIONS = ['wav']
ML_WEIGHTS = []
NAMES = []

app = Flask(__name__)
app.secret_key = "YouWillNeverGuessTheSecretKey"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_file(filename):
    """
    Checks if the name of the file uploaded has an allowable extension type
    :param filename: The name of the file uploaded by the user
    :return: True if the file is of valid extension type, otherwise return False
    """
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/', methods=['GET'])
def index():
    """
    Loads index.html template page to the client
    :return: Response object that with the template page index.html rendered
    """
    return render_template("index.html", audio_link=session.get('uploaded_file'))


@app.route('/uploader', methods=['POST'])
def uploader():
    """
    Handles file uploading to the server
    :return: Redirect to the index() routing function with appropriate flash messages
    """
    if 'file' not in request.files:
        flash("There is no file part in the request")
        return redirect(url_for('index'))

    file_fn = request.files['file']

    if file_fn.filename == '':
        flash("No file has been selected")
        return redirect(url_for('index'))

    if file_fn and allowed_file(file_fn.filename):
        filename = secure_filename(file_fn.filename)
        file_fn.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        session['uploaded_file'] = "/static/uploads/" + filename
        session['uploaded_filename'] = filename

        flash('File uploaded successfully')
        return redirect(url_for('index'))

    flash('You tried to upload unsupported file')
    return redirect(url_for('index'))


@app.route('/filtering', methods=['GET', 'POST'])
def filtering():
    """
    Handles the filtering of the input file and returns the filtered file
    to the client for playback
    :return: Redirection to the index() routing function with the link to the
    filtered audio file passed as an argument
    """
    if request.method == 'GET':
        return redirect(url_for('index'))
    else:
        if request.form['filter'] == 'None':
            flash("You have selected no filter")
        else:
            selected_filter = request.form['filter']
            num_iter = int(request.form['numIter'])
            link = fi.filter_and_save(FILTER_FUNCTIONS.get(selected_filter), UPLOAD_FOLDER, session.get('uploaded_filename'), num_iter)
            flash("You have applied the %s Filter %d times" % (selected_filter, num_iter))
            return render_template('index.html', audio_link=link)

        return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
