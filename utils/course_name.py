import re


def extract_course_title(url: str) -> str:
    """
    Extract and format the LinkedIn Learning course title from a given URL.
    Example:
        Input:  https://www.linkedin.com/learning/typescript-for-javascript-developers
        Output: Typescript For Javascript Developers
    """
    # Extract the last part of the URL after /learning/
    match = re.search(r'/learning/([^/?#]+)', url)
    if not match:
        return "Invalid LinkedIn Learning URL"

    slug = match.group(1)

    # Remove numeric course IDs (e.g., -2021, -25309312)
    slug = re.sub(r'-\d+$', '', slug.strip())

    # Split by hyphen and capitalize each word
    words = slug.split('-')
    title = ' '.join(word.capitalize() for word in words)

    return title


if __name__ == "__main__":
    # Ask user for input URL
    url = input("Enter LinkedIn Learning URL: ").strip()
    print(extract_course_title(url))
