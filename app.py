from flask import Flask, render_template, request, redirect, url_for, session
from werkzeug.utils import secure_filename
import os
import pytesseract
from PIL import Image
import pandas as pd

app = Flask(__name__)
app.secret_key = 'your_secret_key'
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

USERNAME = 'pratap'
PASSWORD = 'report'

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.form['username'] == USERNAME and request.form['password'] == PASSWORD:
            session['logged_in'] = True
            return redirect(url_for('welcome'))
        else:
            return render_template('login.html', error='Invalid credentials')
    return render_template('login.html')

@app.route('/welcome', methods=['GET', 'POST'])
def welcome():
    if not session.get('logged_in'):
        return redirect(url_for('login'))

    extracted_text = None
    if request.method == 'POST':
        file = request.files['image']
        if file:
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)

            image = Image.open(filepath)
            extracted_text = pytesseract.image_to_string(image)

            excel_path = 'extracted_data.xlsx'
            df = pd.DataFrame([[filename, extracted_text]], columns=['Filename', 'ExtractedText'])
            if os.path.exists(excel_path):
                df_existing = pd.read_excel(excel_path, engine='openpyxl')
                df_combined = pd.concat([df_existing, df], ignore_index=True)
                df_combined.to_excel(excel_path, index=False, engine='openpyxl')
            else:
                df.to_excel(excel_path, index=False, engine='openpyxl')

    return render_template('welcome.html', extracted_text=extracted_text)

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
