import os

def extract_course_url(module_url: str) -> str:
    """
    Extract the course base URL from a LinkedIn Learning module URL.
    Example:
      input:  https://www.linkedin.com/learning/course-name/module-name
      output: https://www.linkedin.com/learning/course-name
    """
    parts = module_url.strip().split('/')
    if len(parts) > 5:
        return '/'.join(parts[:5])
    return module_url.strip()


def main():
    # Ask for input file path
    input_path = input("Enter the full path to the input text file: ").strip()

    if not os.path.isfile(input_path):
        print("❌ Error: File not found.")
        return

    # Read URLs from input file
    with open(input_path, 'r', encoding='utf-8') as infile:
        module_urls = [line.strip() for line in infile if line.strip()]

    # Extract course URLs
    course_urls = [extract_course_url(url) for url in module_urls]

    # Create output file path in the same directory
    base, ext = os.path.splitext(input_path)
    output_path = f"{base}_courses{ext}"

    # Write course URLs to output file
    with open(output_path, 'w', encoding='utf-8') as outfile:
        outfile.write('\n'.join(course_urls))

    print(f"✅ Course URLs saved to: {output_path}")


if __name__ == "__main__":
    main()
