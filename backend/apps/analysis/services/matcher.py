from apps.resumes.services.extractor import extract_skills

def match_resume_with_job(resume_skills, job_description):
    job_skills = extract_skills(job_description)

    matched = set(resume_skills) & set(job_skills)
    missing = set(job_skills) - set(resume_skills)

    if len(job_skills) == 0:
        match_score = 0
    else:
        match_score = (len(matched) / len(job_skills)) * 100

    return {
        "match_score": round(match_score, 2),
        "matched_skills": list(matched),
        "missing_skills": list(missing)
    }