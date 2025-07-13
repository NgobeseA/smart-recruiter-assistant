import spacy

nlp = spacy.load('en_core_web_sm')
def semantic_score(cv_text, job_description):
    cv_doc = nlp(cv_text)
    job_doc = nlp(job_description)

    similarity = cv_doc.similarity(job_doc)
    return round(similarity * 100, 2)

def match_skills(cv_text, required_skills):
    cv_doc = nlp(cv_text)
    matches = []
    for skill in required_skills:
        skill_doc = nlp(skill)
        for word in cv_doc:
            if skill_doc.similarity(word) > 0.85:
                matches.append(skill)
                break
    return matches