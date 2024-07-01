import os
import glob

def get_files_from_directory(directory):
    """
    获取文件夹中的所有文件。

    Args:
    directory (str): 文件夹路径。

    Returns:
    list: 文件路径列表。
    """
    # 获取文件夹中的所有文件（不包括子文件夹中的文件）
    files = glob.glob(os.path.join(directory, '*'))
    return files

def get_latest_file(files):
    """
    找到最新的文件。

    Args:
    files (list): 文件路径列表。

    Returns:
    str: 最新文件的路径。
    """
    if not files:
        return None
    
    # 找到修改时间最新的文件
    latest_file = max(files, key=os.path.getmtime)
    return latest_file

def main(directory):
    """
    主函数，读取文件夹中的文件，并找到最新的文件。

    Args:
    directory (str): 文件夹路径。
    """
    files = get_files_from_directory(directory)
    print(f"Files in the directory: {files}")
    latest_file = get_latest_file(files)
    
    if latest_file:
        print(f"The latest file is: {latest_file}")
    else:
        print("No files found in the directory.")

if __name__ == "__main__":
    # 设置文件夹路径
    directory_path = "C:\\UISlicer\\TemplateCAM\\templatecam\\output\\NextVision\\Silicon"
    main(directory_path)
