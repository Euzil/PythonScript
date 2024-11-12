import os

# 循环创建n个文件夹
for i in range(1, 15):
    # 将数字转换为字符串作为文件夹名
    folder_name = str(i)
    
    try:
        # 如果文件夹不存在，则创建
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)
            print(f"成功创建文件夹: {folder_name}")
        else:
            print(f"文件夹 {folder_name} 已存在")
    except Exception as e:
        print(f"创建文件夹 {folder_name} 时出错: {str(e)}")

print("所有文件夹创建完成")