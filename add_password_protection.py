import PyPDF2

def add_password_protection(input_path, output_path, password):
    # 打开要加密的PDF文件
    with open(input_path, 'rb') as f:
        pdf_reader = PyPDF2.PdfFileReader(f)
        pdf_writer = PyPDF2.PdfFileWriter()

        # 复制所有页面到写入器对象
        for page_num in range(pdf_reader.numPages):
            page = pdf_reader.getPage(page_num)
            pdf_writer.addPage(page)

        # 为PDF文件设置密码
        pdf_writer.encrypt(password)

        # 写入加密后的PDF到输出文件
        with open(output_path, 'wb') as output_file:
            pdf_writer.write(output_file)

# 请替换为自己的文件路径和密码
input_pdf_path = 'input.pdf'
output_pdf_path = 'protected.pdf'
password = 'your_password'
add_password_protection(input_pdf_path, output_pdf_path, password)