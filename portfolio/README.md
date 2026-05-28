# Vedant Deodikar — Flask Portfolio

A modern, animated portfolio built with **Flask + HTML + CSS + Bootstrap 5**.

## Sections
Home · About · Projects · Skills/Tools · Contact · Resume download

## Run locally
```bash
pip install -r requirements.txt
python app.py
```
Open http://127.0.0.1:5000

## Add your photo
Drop your picture into `static/img/profile.jpg` (recommended 800×1000 px).
Until you add one, a placeholder shows automatically.

## Project structure
```
portfolio/
├── app.py
├── requirements.txt
├── templates/
│   ├── base.html
│   └── index.html
└── static/
    ├── css/style.css
    ├── js/main.js
    ├── img/        ← put profile.jpg here
    └── resume/Vedant_Resume.pdf
```

## Customize
All site content lives in the dictionaries at the top of `app.py`
(`PROFILE`, `PROJECTS`, `SKILLS`, `ACHIEVEMENTS`) — edit there, no template
changes needed.
