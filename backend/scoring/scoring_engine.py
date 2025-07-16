import spacy
import re

nlp = spacy.load('en_core_web_sm')

def clean_text(text_content):
    return re.sub(r"\s+", " ", text_content.strip().lower())

def semantic_score(cv_text, job_description):
    try:
        cv_doc = nlp(clean_text(cv_text))
        job_doc = nlp(clean_text(job_description))
        similarity = cv_doc.similarity(job_doc)
        return round(similarity * 100, 2)
    except Exception as e:
        return 0.0

def match_skills(cv_text, required_skills):
    cv = clean_text(cv_text)
    req_skills = clean_text(required_skills)
    cv_doc = nlp(cv)
    matched_skills = []

    for skill in req_skills:
        skill_doc = nlp(skill)
        if any(skill_doc.similarity(token) > 0.85 for token in cv_doc):
            matched_skills.append(skill)
    missing_skills = list(set(required_skills) - set(matched_skills))

    return {
        'matched_skills': matched_skills,
        'missing_skills': missing_skills
    }

def evaluate_resume(cv_text, job_description, required_skills):
    score = semantic_score(cv_text, job_description)
    skill_match = match_skills(cv_text, required_skills)

    return {
        'semantic_score': score,
        'matched_skills': skill_match['matched_skills'],
        'missing_skills': skill_match['missing_skills']
    }