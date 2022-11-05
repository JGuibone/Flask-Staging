from os.path import join
from flask import Flask, request, redirect, render_template
from werkzeug.utils import secure_filename
from pathlib import Path
from website.PyScripts.MainTextExtModule import PDFObject, DocxToText


def create_app():
    UPLOAD_FOLDER = Path("website/uploads")
    ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'doc', 'docx', 'ppt', 'pptx', 'mp3', 'mkv', 'mp4'}

    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'ifY9%N3^8iyD*q&zdBWNWMB8WK#Q6@7PycrzukRPjW5c^7sv&$c6e3mAn^aVbWGy'
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
    app.config['MAX_CONTENT_LENGTH'] = 22 * 1000 * 1000

    def allowed_file(filename):
        return filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
    
    @app.route("/")
    def index():
        return render_template('home.html')

    @app.route('/uploader', methods=['POST'])
    def uploader():
        if request.method == 'POST':
            textExctLoc = Path("website/textExtract")
            files = request.files.getlist('file')
            for file in files:
                if 'file' not in request.files or file.filename == '':
                    continue
                if allowed_file(file.filename) == True:
                    match file.filename.rsplit('.', 1)[1].lower():
                        case "pdf":
                            file.save(Path(join(UPLOAD_FOLDER,secure_filename(file.filename))))
                            PDFObject(textExctLoc,file)
                        case "docx":
                            file.save(Path(join(UPLOAD_FOLDER,secure_filename(file.filename))))
                            DocxToText(textExctLoc,file)
                        case "txt":
                            print("the number is "+str(test1)+".")
                    
        return 'you are on the upload route'

    return app