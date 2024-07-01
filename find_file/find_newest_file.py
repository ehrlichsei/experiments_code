import os
from datetime import datetime

def find_newest_file(folder_path):
    newest_file = None
    newest_mtime = None

    # 遍历文件夹及其子文件夹
    for root, dirs, files in os.walk(folder_path):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            try:
                # 获取文件最后修改时间
                mtime = os.path.getmtime(file_path)
                # 转换为可读的时间格式
                last_modified = datetime.fromtimestamp(mtime)

                # 判断是否为最新文件
                if newest_mtime is None or mtime > newest_mtime:
                    newest_mtime = mtime
                    newest_file = file_path

            except OSError as e:
                print(f"Error accessing {file_path}: {e}")

    return newest_file

# 示例用法
folder_path = "C:\\UISlicer\\TemplateCAM\\templatecam\\output"
newest_file = find_newest_file(folder_path)

if newest_file:
    print(f"The newest file is: {newest_file}")
else:
    print("No files found.")
