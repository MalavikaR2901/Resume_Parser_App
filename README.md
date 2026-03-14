**RESUME PARSER APP**

It is a web based resume parser that automatically extracts candidate's resume using Natural Language Processing (NLP). 
This application allows users to allows users to upload (there is drag and drop facility) resume end extract details such as name, skill, company, education etc. 
It helps the recruiters to automate resume screening process and simplifies resume screening process. 

*Features**

* Upload resumes in PDF format
* Extract important information from resumes
* Identify candidate skills
* Simple and user-friendly web interface
* Fast resume parsing using Python

*Tech Stack**

* Python flask 
* ollama (Local LLM for resume analysis)
* HTML CSS

*Project Structure**

'''
resume_parser_using_python
|
├── __DATA__
|      |
|      ├──file.pdf
├── static
|      |
|      ├── logo.png
├── templates
|      |
|      ├── index.html
|      ├──login.html
|      ├── register.html
├── app.py
├── requirements.txt
├── resume_parser.py
├── skills.txt

'''

*Installation**

* Clone the repository

git clone https://github.com/MalavikaR2901/Resume_Parser_App.git

* Move into the project folder

    cd Resume_Parser_App

* Create virtual environment

    python -m venv venv

* Activate environment

   Windows: venv\Scripts\activate

* Install dependencies

    pip install -r requirements.txt

=*Run the Application**

* python app.py

* Open the browser and go to http://localhost:5000

Author

Malavika R
contact : www.linkedin.com/in/malavikar2001

MCA Student | Machine Learning & AI Enthusiast       

