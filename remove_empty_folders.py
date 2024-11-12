import os

def remove_empty_folders(directory_path):
    # 遍历目录树
    for root, dirs, files in os.walk(directory_path, topdown=False):
        for folder in dirs:
            folder_path = os.path.join(root, folder)
            # 如果目录为空，则删除
            if not os.listdir(folder_path):
                os.rmdir(folder_path)

# 替换下面的路径为自己想清理的目录的路径
remove_empty_folders('your_directory_path')