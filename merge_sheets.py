import pandas as pd

def merge_sheets(file_path, output_file_path):
    # 打开Excel文件
    xls = pd.ExcelFile(file_path)
    # 创建一个空的DataFrame
    df = pd.DataFrame()

    # 遍历所有工作表
    for sheet_name in xls.sheet_names:
        # 读取每个工作表
        sheet_df = pd.read_excel(xls, sheet_name)
        # 将每个工作表的数据追加到df中
        df = df.append(sheet_df, ignore_index=True)

    # 将合并后的数据写入新的Excel文件
    df.to_excel(output_file_path, index=False)

# 替换为自己的文件路径
merge_sheets('path_to_your_excel_file.xlsx', 'path_to_your_output_file.xlsx')