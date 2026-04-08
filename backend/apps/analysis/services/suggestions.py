def generate_suggestions(match_score, missing_skills, resume_skills):
    suggestions = []

    # 🔥 Low match score
    if match_score < 50:
        suggestions.append("Your resume has low relevance to the job. Consider tailoring it.")

    # 🔥 Missing skills
    if missing_skills:
        suggestions.append(f"Consider adding these skills: {', '.join(missing_skills)}")

    # 🔥 Weak skillset
    if len(resume_skills) < 5:
        suggestions.append("Add more relevant technical skills to strengthen your profile.")

    # 🔥 Strong profile
    if match_score > 80:
        suggestions.append("Your resume is well aligned with the job. Minor improvements can boost your chances.")

    return suggestions