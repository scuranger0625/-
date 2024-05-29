#GPT對話翻譯.py

#這個程式的主要功能是將給定的文本翻譯成中文。它使用 OpenAI 的 GPT-3.5 模型，
#將輸入的文本視為英文，然後通過生成式對話方式進行翻譯。它會將給定的英文文本作為輸入，然後生成相應的中文翻譯。

import openai

openai.api_key = "sk-proj-tXsJfPWYz4cI3CLAObzIT3BlbkFJ9POG15DPqqkeEFaNpYR3"

def translate_to_chinese(text):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Translate the following text into Chinese:"},
            {"role": "user", "content": text}
        ],
        temperature=0.7,
        max_tokens=200
    )
    return response.choices[0].message['content']

# 示例
input_text = "Translate the following text into Chinese:\n\nHello, how are you?"
translation = translate_to_chinese(input_text)
print('翻译结果:', translation)


