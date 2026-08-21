# 🤖 AI-Powered Resume Ranker

![Python](https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python)
![Flask](https://img.shields.io/badge/Flask-Web%20Framework-black?style=for-the-badge&logo=flask)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML-orange?style=for-the-badge&logo=scikit-learn)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5-purple?style=for-the-badge&logo=bootstrap)

## 📌 Project Overview

AI-Powered Resume Ranker is an intelligent Applicant Tracking System (ATS) built using **Flask, Natural Language Processing (NLP), TF-IDF, and Cosine Similarity**.

The application helps recruiters automatically compare multiple resumes with a job description and rank candidates based on their relevance.

Instead of manually reviewing hundreds of resumes, recruiters can upload a job description and multiple PDF resumes. The system analyzes them, calculates ATS scores, extracts technical skills, generates recommendations, and creates a professional HR report.

---

# 🚀 Features

✅ Upload multiple PDF resumes

✅ Upload Job Description

✅ Automatic PDF text extraction

✅ NLP Text Preprocessing

✅ TF-IDF Vectorization

✅ Cosine Similarity Matching

✅ ATS Score Calculation

✅ Resume Ranking

✅ Skill Extraction

✅ Recommendation System

✅ Professional HR Dashboard

✅ Top 3 Candidate Cards

✅ Interactive ATS Score Chart

✅ Drag & Drop Resume Upload

✅ Excel Report Generation

✅ Responsive UI

✅ Custom 404 Page

---

# 🖼️ Screenshots

Add your screenshots inside the `screenshots/` folder.

### 🏠 Home Page

![Home](screenshots/home.png)

### 📊 Dashboard

![Dashboard](screenshots/results.png)

### 📈 ATS Score Chart

![Chart](screenshots/chart.png)

### 📄 Excel Report

![Excel](screenshots/excel_report.png) 
---

# 🛠️ Tech Stack

### Backend
- Python
- Flask

### Machine Learning & NLP
- Scikit-learn
- TF-IDF Vectorizer
- Cosine Similarity
- SpaCy

### Data Processing
- NumPy
- Pandas
- PyPDF2

### Report Generation
- OpenPyXL

### Frontend
- HTML5
- CSS3
- Bootstrap 5
- JavaScript
- Chart.js

---

# 📂 Project Structure

```text
AI-Powered-Resume-Ranker/
│
├── app.py
├── requirements.txt
├── README.md
│
├── uploads/
├── reports/
├── screenshots/
│
├── static/
│   └── style.css
│
├── templates/
│   ├── index.html
│   ├── results.html
│   ├── about.html
│   └── 404.html
│
└── utils/
    ├── __init__.py
    ├── pdf_reader.py
    ├── text_preprocessor.py
    ├── resume_ranker.py
    ├── report_generator.py
    └── skill_extractor.py
```

---

# ⚙️ Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/AI-Powered-Resume-Ranker.git
```

2. Move into the project folder:

```bash
cd AI-Powered-Resume-Ranker
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run the application:

```bash
python app.py
```

5. Open your browser and visit:

```text
http://127.0.0.1:5000
```

---

# 💡 How It Works

1. Enter or paste a Job Description.
2. Upload one or more PDF resumes.
3. The application extracts text from each resume.
4. NLP preprocessing cleans the text.
5. TF-IDF converts text into numerical vectors.
6. Cosine Similarity compares each resume with the Job Description.
7. ATS scores are calculated.
8. Candidates are ranked automatically.
9. Skills and recommendations are displayed.
10. A downloadable Excel HR report is generated.

---

# 🚀 Future Improvements

- Resume keyword highlighting
- AI-generated candidate summaries
- Resume preview before analysis
- Login and recruiter dashboard
- Database integration
- Cloud deployment
- Multi-language resume support

---

# 👨‍💻 Author

**Pavan Shantilal**

B.Tech – Computer Science & Engineering (AI & ML)

---

# 📄 License

This project is developed for educational purposes, internship submissions, and portfolio demonstrations.