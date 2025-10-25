import os


def get_unique_urls(file_path):
    try:
        # Read all URLs from the input file
        with open(file_path, 'r', encoding='utf-8') as file:
            urls = [line.strip() for line in file if line.strip()]

        # Remove duplicates while preserving order
        seen = set()
        unique_urls = []
        for url in urls:
            if url not in seen:
                seen.add(url)
                unique_urls.append(url)

        # Create output file path in same directory
        base, ext = os.path.splitext(file_path)
        output_file = f"{base}_unique{ext}"

        # Write unique URLs to new file
        with open(output_file, 'w', encoding='utf-8') as file:
            file.write("\n".join(unique_urls))

        print(f"\n✅ Unique URLs written to: {output_file}")

    except FileNotFoundError:
        print(f"\n❌ Error: File not found at '{file_path}'")
    except Exception as e:
        print(f"\n⚠️ An error occurred: {e}")


if __name__ == "__main__":
    default_file = r"C:\Temp\input.txt"
    user_input = input(f"Enter input file path (press Enter for default: {default_file}): ").strip()

    # Use default if no input provided
    file_path = user_input if user_input else default_file

    get_unique_urls(file_path)
