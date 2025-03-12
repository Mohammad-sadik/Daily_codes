import PyPDF2
import re
import spacy
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity



nlp = spacy.load("en_core_web_sm")


def extract_text_from_pdf(resume_path):
    try:
        with open(resume_path, "rb") as file:
            reader = PyPDF2.PdfReader(file)
            text = "".join([page.extract_text() or "" for page in reader.pages])
            return clean_text(text)
    except Exception as e:
        print(f"Error reading PDF: {e}")
        return ""

def clean_text(text):
    text = re.sub(r'\s+', ' ', text)  # Remove spaces/newlines
    text = re.sub(r'[^\x00-\x7F]+', '', text)  # Remove non-ASCII char
    return text.strip()

def match_resume_with_job(resume_text, job_desc):
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform([resume_text, job_desc])
    similarity = cosine_similarity(vectors)[0][1]
    return similarity


pdf_path = input("Enter full path of Resume: ")
resume_text = extract_text_from_pdf(pdf_path)
job_description = "Proven understanding of a software development language (e.g. C# Java) or scripting language (e.g. Python JavaScript) and of software development methodology. Knowledge of web services and hands-on experience with web service testing tools such as SoapUI. Hands on experience with Microsoft SQL. Understanding of software development methodologyand a strong understanding of backend (non UI) testing."
score = match_resume_with_job(resume_text, job_description)
print(f"Resume match score: {score*100:.2f}%")
