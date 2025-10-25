import re

def extract_course_title(url: str) -> str:
    match = re.search(r'/learning/([^/?#]+)', url)
    if not match:
        return "Invalid LinkedIn Learning URL"

    slug = match.group(1).strip()

    # Remove only long numeric IDs (6+ digits), not years like 2021
    slug = re.sub(r'-\d{6,}$', '', slug)

    words = slug.split('-')
    title = ' '.join(word.capitalize() for word in words)

    return title


# --- Validation Tests ---
urls = [
    "https://www.linkedin.com/learning/learning-java-collections",
    "https://www.linkedin.com/learning/typescript-for-javascript-developers",
    "https://www.linkedin.com/learning/python-quick-start-22667553",
    "https://www.linkedin.com/learning/learning-python-2021",
    "https://www.linkedin.com/learning/learning-python-25309312",
"https://www.linkedin.com/learning/accounting-foundations-budgeting-2019",
"https://www.linkedin.com/learning/accounting-foundations-budgeting-2020",
]

for u in urls:
    print(f"{u}\n→ {extract_course_title(u)}\n")
