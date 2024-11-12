import PyPDF2

def merge_pdfs(input_paths, output_path):
    # 创建PDF合并器对象
    pdf_merger = PyPDF2.PdfMerger()
    
    # 遍历所有输入路径并添加到合并器
    for path in input_paths:
        with open(path, 'rb') as f:
            pdf_merger.append(f)
    
    # 将合并后的PDF写入输出文件
    with open(output_path, 'wb') as f:
        pdf_merger.write(f)

# 替换为自己的PDF文件路径
input_pdf_paths = ['pdf1.pdf', 'pdf2.pdf', 'pdf3.pdf']
output_pdf_path = 'merged.pdf'
merge_pdfs(input_pdf_paths, output_pdf_path)