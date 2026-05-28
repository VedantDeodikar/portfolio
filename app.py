"""
Vedant Deodikar — Portfolio (Flask)
Run:  pip install flask  &&  python app.py
Then open http://127.0.0.1:5000
"""
from flask import Flask, render_template, request, send_from_directory, flash, redirect, url_for
import os

app = Flask(__name__)
app.secret_key = "change-this-secret-key"

# ---------- Site data (edit freely) ----------
PROFILE = {
    "name": "Vedant Deodikar",
    "role": "Aspiring Software Engineer  ·  B.Tech E&TC Student",
    "tagline": "I build intelligent solutions with Python and Machine Learning.",
    "email": "vedantdeodikar04@gmail.com",
    "linkedin": "https://linkedin.com/in/vedant-deodikar-18482b259",
    "github": "https://github.com/",
    "location": "Solapur, India",
    "about": (
        "I'm a Python Full-Stack Developer passionate about building intelligent "
"and scalable software solutions. I enjoy working with machine learning, "
"data analytics, and modern web technologies to create applications that "
"solve real-world problems. From developing AI-powered systems to building "
"responsive full-stack applications and interactive dashboards, I focus on "
"writing clean, efficient, and impactful code while continuously expanding "
"my expertise in data, AI, and software development."

    ),
    "education": [
        {"school": "Walchand Institute of Technology",
         "detail": "B.Tech in Electronics & Telecommunication",
         "score": "CGPA 9.59", "year": "Present"},
        {"school": "Sangameshwar College, Solapur",
         "detail": "Class XII — State Board",
         "score": "75.17%", "year": ""},
        {"school": "Indian Model School",
         "detail": "Class X — State Board",
         "score": "94.4%", "year": ""},
    ],
}

PROJECTS = [
    {
        "title": "Smart Attendance System Using Face Recognition",
        "description": (
            "Wireless smart attendance system built with Flask, OpenCV and "
            "Raspberry Pi 4. Real-time contactless tracking with SQLite "
            "storage and an intuitive analytics dashboard that auto-generates "
            "reports — eliminating manual roll-call effort."
        ),
        "tags": ["Flask", "OpenCV", "Raspberry Pi", "SQLite", "Python"],
        "icon": "bi-camera-video",
    },
    {
        "title": "Career Prediction Model",
        "description": (
            "Interactive ML platform that recommends personalized career "
            "paths from a student's skills, interests and iterative feedback. "
            "Built with Python & Scikit-learn, it delivers multi-week guidance, "
            "career insights and rich data visualizations."
        ),
        "tags": ["Python", "Scikit-learn", "Machine Learning", "Data Viz"],
        "icon": "bi-graph-up-arrow",
    },
]

SKILLS = {
    "Languages":  ["C", "Java", "Python", "HTML", "CSS", "JavaScript"],
    "Frameworks": ["Flask", "Django"],
    "Database":   ["MySQL", "SQLite"],
    "Tools":      ["Tableau", "Power BI", "Git", "VS Code"],
    "Soft Skills":["Leadership", "Teamwork", "Multilingual Communication"],
}

ACHIEVEMENTS = [
    "ISTE Program Coordinator — organized Yuva Darpan & annual prize distribution",
    "WITCHAR-2k25 Coordinator — organized Quizotronics event",
    "Participant — Meshmerize, Techfest IIT Bombay",
    "Runner-up — Engineer's Day Aptitude Competition, WIT Solapur",
]

# ---------- Routes ----------
@app.route("/")
def home():
    return render_template("index.html",
                           profile=PROFILE,
                           projects=PROJECTS,
                           skills=SKILLS,
                           achievements=ACHIEVEMENTS)

@app.route("/download-resume")
def download_resume():
    return send_from_directory(
        os.path.join(app.root_path, "static", "resume"),
        "Vedant_Resume.pdf",
        as_attachment=True,
    )

@app.route("/contact", methods=["POST"])
def contact():
    name    = request.form.get("name", "").strip()
    email   = request.form.get("email", "").strip()
    message = request.form.get("message", "").strip()
    if not (name and email and message):
        flash("Please fill in all fields.", "danger")
    else:
        # In production: send an email or store in DB.
        print(f"[CONTACT] {name} <{email}>: {message}")
        flash("Thanks for reaching out! I'll get back to you soon.", "success")
    return redirect(url_for("home") + "#contact")

if __name__ == "__main__":
    app.run(debug=True)
