def calculate_ats_score(match_score, resume_skills):
    base_score = match_score

    # Bonus for more skills
    bonus = min(len(resume_skills) * 2, 20)

    ats_score = base_score + bonus

    return min(round(ats_score, 2), 100)