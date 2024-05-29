#PDF文字提取與翻譯.py

#讀取PDF文件：通過使用PyPDF2庫，從指定的PDF文件中提取文本內容。
#將文本翻譯成中文：將每個文本塊作為輸入，使用OpenAI的GPT-3.5模型將其翻譯成中文。
#打印翻譯結果：將翻譯後的中文文本打印到控制台上。
#這個腳本可以幫助用戶快速地將PDF文件中的文本翻譯成中文，並且可以應用於各種需要進行PDF文本翻譯的場景中。

import openai
from PyPDF2 import PdfReader
import os

# 设置 OpenAI API 密钥
openai.api_key = "sk-proj-tXsJfPWYz4cI3CLAObzIT3BlbkFJ9POG15DPqqkeEFaNpYR3"

# 读取 PDF 文件
def read_pdf(file_path):
    with open(file_path, 'rb') as f:
        reader = PdfReader(f)
        number_of_pages = len(reader.pages)
        chunks = []

        for i in range(number_of_pages):
            page = reader.pages[i]
            text = page.extract_text()
            chunks.append(text)

        return chunks

# 接受用户输入的PDF文件路径
pdf_file_path = input("请输入PDF文件的路径：")

# 读取PDF文件
pdf_chunks = read_pdf(pdf_file_path)

# 打印PDF文件的内容
for chunk in pdf_chunks:
    # 输出原文
    print('原文:', chunk)
    
    # 翻译内容
    response = openai.Completion.create(
        engine="gpt-3.5-turbo",
        prompt=f"Translate the following text into Chinese:\n\n{chunk}",
        temperature=0.7,
        max_tokens=200,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0,
        stop=["\n"]
    )
    
    # 输出翻译结果
    print('翻译结果:', response.choices[0].text.strip())


















