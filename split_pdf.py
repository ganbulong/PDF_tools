import fitz  # PyMuPDF库
import os  # 导入os模块

# 指定输入PDF文件和输出PDF文件
input_pdf_path = "F:\Python代码\练习项目\demo1\研究生学术英语读写教程.pdf"  # 替换为你的输入PDF文件路径
output_pdf_path = "F:\Python代码\练习项目\demo1\中文作业.pdf"  # 替换为你的输出PDF文件路径

# 自定义拆分的页范围（从第3页到第6页）
start_page = 3
end_page = 4

# 使用PyMuPDF打开输入PDF文件
pdf_document = fitz.open(input_pdf_path)

# 创建一个新的PDF文档用于存储合并的页面
output_pdf_document = fitz.open()

# 合并指定页范围内的页面到新的PDF文档
for page_number in range(start_page - 1, end_page):
    page = pdf_document.load_page(page_number)
    output_pdf_document.insert_pdf(pdf_document, from_page=page_number, to_page=page_number)

# 保存新的PDF文件
output_pdf_document.save(output_pdf_path)

# 关闭输入和输出PDF文件
pdf_document.close()
output_pdf_document.close()
