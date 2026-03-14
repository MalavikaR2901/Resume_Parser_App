# FLASK APP - Run the app using flask --app app.py run
import os, sys
from flask import Flask, request, render_template
from pypdf import PdfReader 
import json
from werkzeug.utils import secure_filename
from resume_parser import ats_extractor
from flask import redirect, url_for
# sys.path.insert(0, os.path.abspath(os.getcwd()))


UPLOAD_PATH = r"__DATA__"
if not os.path.exists(UPLOAD_PATH):
    os.makedirs(UPLOAD_PATH)

app = Flask(__name__)

def _read_file_from_path(path):
    try:
        reader = PdfReader(path) 
        text = ""
        for page in reader.pages:
            content = page.extract_text()
            if content:
                text += content
        return text
    except Exception as e:
        print(f"Extraction Error: {e}")
        return ""

@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        password = request.form["password"]

        print(name, email, password)  # just for testing

        # After register → go to login page
        return redirect(url_for("login"))

    return render_template("register.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        print(email, password)

        return render_template("index.html")

    return render_template("login.html")
@app.route('/')
def index():
    return render_template('index.html', data=None)

@app.route("/process", methods=["POST"])
def ats():
    if 'pdf_doc' not in request.files:
        return render_template('index.html', data={"Error": "No file uploaded"})
    doc = request.files['pdf_doc']
    if doc.filename == '':
        return render_template('index.html', data={"Error": "No file selected"})
    filename = secure_filename(doc.filename)
    doc_path = os.path.join(UPLOAD_PATH, filename)
    doc.save(doc_path)
    raw_text = _read_file_from_path(doc_path)
    if not raw_text.strip():
        return render_template('index.html', data={"Error": "Empty PDF"})
    
    # 4. Process with AI (Local Ollama or Gemini)
    data = ats_extractor(raw_text)
    return render_template('index.html', data=data)
    
if __name__ == "__main__":
    app.run(port=8000, debug=True)
