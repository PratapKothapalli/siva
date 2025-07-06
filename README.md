# Project Status Report Web App

This is a Flask-based web application that allows authenticated users to upload multiple images, extract structured data using OCR, and generate an Excel report. The app is designed to be deployed on Render.

---

## 🔐 Features

- User authentication (username: `pratap`, password: `report`)
- Upload multiple image files (`.jpg`, `.jpeg`, `.png`)
- Extract project data from images using OCR (`pytesseract`)
- Generate and download an Excel report (`project_status_report.xlsx`)
- Deployable on Render with `gunicorn`

---

## ⚙️ Setup Instructions (Local)

### 1. Clone the Repository

```bash
git clone https://github.com/PratapKothapalli/siva.git
cd siva

