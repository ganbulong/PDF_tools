import fitz  # PyMuPDF库

# 打开PDF文件
pdf_file_path = "测试.pdf"
pdf_document = fitz.open(pdf_file_path)

# 提取文字内容
text = ""
for page_num in range(pdf_document.page_count):
    page = pdf_document.load_page(page_num)
    text += page.get_text()

# 关闭PDF文件
pdf_document.close()

# 打印提取的文字内容
print(text)
