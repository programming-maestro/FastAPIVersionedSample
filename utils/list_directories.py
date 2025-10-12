import os


def list_directories(path):
    """
    List all directory names from the given path.
    Works on Windows, macOS, and Linux.
    """
    try:
        # Normalize the path (handles forward/back slashes)
        path = os.path.expanduser(path)
        path = os.path.abspath(path)

        if not os.path.exists(path):
            print(f"Error: The path '{path}' does not exist.")
            return []

        # List directories only
        directories = [
            name for name in os.listdir(path)
            if os.path.isdir(os.path.join(path, name))
        ]

        print(f"Directories in '{path}':")
        for d in directories:
            print(" -", d)

        return directories

    except Exception as e:
        print(f"An error occurred: {e}")
        return []


if __name__ == "__main__":
    # Example usage:
    user_path = input("Enter the directory path: ").strip()
    list_directories(user_path)
