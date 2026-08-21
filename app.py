from flask import (
    Flask,
    render_template,
    request,
    send_file,
    redirect,
    url_for,
    flash
)

import os

from werkzeug.utils import secure_filename

from utils.pdf_reader import extract_text_from_pdf
from utils.text_preprocessor import preprocess_text
from utils.resume_ranker import rank_resumes
from utils.report_generator import generate_excel_report 
from utils.skill_extractor import extract_skills

# ==========================================================
# Flask Configuration
# ==========================================================

app = Flask(__name__)

app.secret_key = "resume_ranker_secret_key"

UPLOAD_FOLDER = "uploads"
REPORT_FOLDER = "reports"

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.config["REPORT_FOLDER"] = REPORT_FOLDER

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(REPORT_FOLDER, exist_ok=True)

ALLOWED_EXTENSIONS = {"pdf"}


# ==========================================================
# Helper Function
# ==========================================================

def allowed_file(filename):

    return (
        "." in filename
        and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS
    )


# ==========================================================
# Routes
# ==========================================================

@app.route("/")
def home():

    return render_template("index.html")


@app.route("/about")
def about():

    return render_template("about.html")


@app.route("/rank", methods=["POST"])
def rank():

    job_description = request.form.get("job_description", "").strip()

    resumes = request.files.getlist("resumes")

    if job_description == "":

        flash("Please enter Job Description.")

        return redirect(url_for("home"))

    if len(resumes) == 0:

        flash("Please upload at least one Resume.")

        return redirect(url_for("home"))

    uploaded_resumes = []

    for resume in resumes:

        if resume.filename == "":

            continue

        if not allowed_file(resume.filename):

            continue

        filename = secure_filename(resume.filename)

        filepath = os.path.join(
            app.config["UPLOAD_FOLDER"],
            filename
        )

        resume.save(filepath)

        resume_text = extract_text_from_pdf(filepath)

        cleaned_text = preprocess_text(resume_text)

        uploaded_resumes.append({

    "name": filename,

    "text": cleaned_text,

    "skills": extract_skills(cleaned_text)

})
        # ==========================================================
    # Preprocess Job Description
    # ==========================================================

    cleaned_job_description = preprocess_text(job_description)

    # ==========================================================
    # Rank Resumes
    # ==========================================================

    ranked_resumes = rank_resumes(

        cleaned_job_description,

        uploaded_resumes

    )

    # ==========================================================
    # Dashboard Statistics
    # ==========================================================

    total = len(ranked_resumes)

    if total > 0:

        top_score = ranked_resumes[0]["score"]

        average = round(

            sum(resume["score"] for resume in ranked_resumes)

            / total,

            2

        )

    else:

        top_score = 0

        average = 0

    # ==========================================================
    # Generate Excel Report
    # ==========================================================

    report_path = generate_excel_report(

        ranked_resumes,

        app.config["REPORT_FOLDER"]

    )

    # Save report path for download

    app.config["LATEST_REPORT"] = report_path

    # ==========================================================
    # Render Results Page
    # ==========================================================

    return render_template(

        "results.html",

        ranked_resumes=ranked_resumes,

        total=total,

        top_score=top_score,

        average=average

    )


# ==========================================================
# Download Report
# ==========================================================

@app.route("/download_report")
def download_report():

    report_path = app.config.get("LATEST_REPORT")

    if report_path and os.path.exists(report_path):

        return send_file(

            report_path,

            as_attachment=True

        )

    flash("No report available. Please analyze resumes first.")

    return redirect(url_for("home"))


# ==========================================================
# Error Pages
# ==========================================================

@app.errorhandler(404)
def page_not_found(error):

    return (

        render_template(

            "404.html"

        ),

        404

    )


@app.errorhandler(500)
def internal_server_error(error):

    return (

        "<h2>500 - Internal Server Error</h2>"
        "<p>Something went wrong. Please try again.</p>",

        500

    )


# ==========================================================
# Run Application
# ==========================================================

if __name__ == "__main__":

    app.run(

        debug=True,

        host="0.0.0.0",

        port=5000

    )