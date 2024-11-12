import pandas as pd

def read_excel(file_path):
    # 读取Excel文件
    df = pd.read_excel(file_path)
    return df

def write_to_excel(data, file_path):
    # 将数据写入Excel文件
    df = pd.DataFrame(data)
    df.to_excel(file_path, index=False)

# 读取Excel文件
dataframe = read_excel('path_to_your_input_file.xlsx')

# 将修改后的数据写入新的Excel文件
write_to_excel(dataframe, 'path_to_your_output_file.xlsx')