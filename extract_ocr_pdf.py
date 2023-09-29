import fitz  # PyMuPDF库
import pytesseract
from PIL import Image
from docx import Document  # 导入python-docx库中的Document类
import os

# 指定扫描版PDF文件路径
pdf_file_path = "文字文稿1.pdf"

# 设置Tesseract OCR可执行文件路径
pytesseract.pytesseract.tesseract_cmd = r'E:\tesseract\tesseract.exe'  # 替换为你的Tesseract安装路径

# 设置TESSDATA_PREFIX环境变量，指向包含traineddata文件的目录
os.environ['TESSDATA_PREFIX'] = r'E:\tesseract\tessdata'  # 替换为你的traineddata文件所在的目录

# 使用PyMuPDF将PDF转换为图像
pdf_document = fitz.open(pdf_file_path)
image_list = []
for page_number in range(len(pdf_document)):
    page = pdf_document.load_page(page_number)
    image = page.get_pixmap()
    image_list.append(image)

# 提取文本内容
text = ""
for image in image_list:
    # 将PyMuPDF图像对象转换为PIL图像对象
    pil_image = Image.frombytes("RGB", [image.width, image.height], image.samples)
    
    # 使用Tesseract进行OCR处理
    # 使用Tesseract进行OCR处理
    page_text = pytesseract.image_to_string(pil_image, lang='chi_sim+chi_tra+eng')

    text += page_text

# 创建一个新的Word文档
doc = Document()

# 添加提取的文本到Word文档中
doc.add_paragraph(text)

# 保存Word文档为.docx文件
doc.save("导出中文6.docx")

# 关闭PDF文档
pdf_document.close()
