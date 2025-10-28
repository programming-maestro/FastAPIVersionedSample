import os

def sort_urls_from_file():
    # Ask user for file path
    file_path = input("Enter the full path of the text file containing URLs: ").strip()

    # Check if file exists
    if not os.path.isfile(file_path):
        print("Error: File not found. Please check the path and try again.")
        return

    # Read URLs from file
    with open(file_path, 'r', encoding='utf-8') as file:
        urls = [line.strip() for line in file if line.strip()]

    # Sort URLs alphabetically
    sorted_urls = sorted(urls)

    # Create output file path (same directory)
    directory = os.path.dirname(file_path)
    output_path = os.path.join(directory, "sorted_urls.txt")

    # Write sorted URLs to new file
    with open(output_path, 'w', encoding='utf-8') as output_file:
        for url in sorted_urls:
            output_file.write(url + '\n')

    print(f"✅ Sorted URLs saved to: {output_path}")

if __name__ == "__main__":
    sort_urls_from_file()
