import os

def list_directories(path):
    """
    List all directory names from the given path.
    """
    path = os.path.abspath(os.path.expanduser(path))
    if not os.path.exists(path):
        print(f"Error: Path '{path}' does not exist.")
        return []

    dirs = [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]
    return dirs

def rename_directory(base_path, old_name, new_name):
    """
    Rename a directory safely, without changing its contents.
    """
    old_path = os.path.join(base_path, old_name)
    new_path = os.path.join(base_path, new_name)

    if not os.path.exists(old_path):
        print(f"Error: '{old_name}' does not exist in '{base_path}'.")
        return False

    if os.path.exists(new_path):
        print(f"Error: '{new_name}' already exists in '{base_path}'.")
        return False

    try:
        os.rename(old_path, new_path)
        print(f"Renamed: '{old_name}' → '{new_name}'")
        return True
    except Exception as e:
        print(f"Failed to rename '{old_name}': {e}")
        return False


if __name__ == "__main__":
    base_path = input("Enter the directory path: ").strip()
    directories = list_directories(base_path)

    if not directories:
        print("No directories found.")
    else:
        print("\nDirectories found:")
        for i, d in enumerate(directories, start=1):
            print(f"{i}. {d}")

        try:
            choice = int(input("\nEnter the number of the folder to rename: "))
            if 1 <= choice <= len(directories):
                old_name = directories[choice - 1]
                new_name = input(f"Enter new name for '{old_name}': ").strip()
                rename_directory(base_path, old_name, new_name)
            else:
                print("Invalid selection.")
        except ValueError:
            print("Please enter a valid number.")
