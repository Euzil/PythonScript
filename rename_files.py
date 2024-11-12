import os

def rename_files(directory_path, old_name, new_name):
    # 遍历目录中的所有文件
    for filename in os.listdir(directory_path):
        # 检查文件名中是否包含旧名称
        if old_name in filename:
            # 生成新的文件名
            new_filename = filename.replace(old_name, new_name)
            # 重命名文件
            os.rename(os.path.join(directory_path, filename), 
                      os.path.join(directory_path, new_filename))

# 替换下面的路径和名称
# 例如 directory_path: 您要重命名文件的目录路径
rename_files('your_directory_path', 'old_name', 'new_name')