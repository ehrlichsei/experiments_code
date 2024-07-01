import os

def find_latest_subdirectory(parent_dir):
    """
    Find the most recently modified subdirectory within a directory.
    
    Args:
    - parent_dir (str): Path to the parent directory to search in.
    
    Returns:
    - str: Path to the most recently modified subdirectory.
    """
    latest_subdir = None
    latest_mod_time = 0
    
    for subdir in os.listdir(parent_dir):
        subdir_path = os.path.join(parent_dir, subdir)
        if os.path.isdir(subdir_path):
            mod_time = os.path.getmtime(subdir_path)
            if mod_time > latest_mod_time:
                latest_mod_time = mod_time
                latest_subdir = subdir_path
    
    return latest_subdir

def find_latest_file_in_directory(directory):
    """
    Find the most recently modified file within a directory and its subdirectories.
    
    Args:
    - directory (str): Path to the directory to search in.
    
    Returns:
    - str: Path to the most recently modified file.
    """
    latest_file = None
    latest_mod_time = 0
    
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            mod_time = os.path.getmtime(file_path)
            if mod_time > latest_mod_time:
                latest_mod_time = mod_time
                latest_file = file_path
    
    return latest_file

# 示例用法
if __name__ == "__main__":
    parent_directory = "C:\\UISlicer\\TemplateCAM\\templatecam\\output"
    
    latest_subdir = find_latest_subdirectory(parent_directory)

    latest_file = find_latest_file_in_directory(latest_subdir)
        if latest_file:
            print(f"The most recently modified file in {latest_subdir}: {latest_file}")
        else:
            print(f"No files found in {latest_subdir}")
    else:
        print(f"No subdirectories found in {parent_directory}")
