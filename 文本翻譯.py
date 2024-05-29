# 文本翻譯.py

#这个程式的主要功能是将给定的文本块列表翻译成中文。它使用 OpenAI 的 GPT-3.5 模型来进行翻译，并将每个文本块翻译成相应的中文文本。

import openai

openai.api_key = "sk-proj-tXsJfPWYz4cI3CLAObzIT3BlbkFJ9POG15DPqqkeEFaNpYR3"

def translate_chunks_to_chinese(chunks):
    translated_chunks = []
    for chunk in chunks:
        prompt = "Translate the following text into Chinese:\n\n" + chunk
        response = openai.Completion.create(
            engine="gpt-3.5-turbo",
            prompt=prompt,
            temperature=0.7,
            max_tokens=200,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0,
            stop=["\n"]
        )
        translated_chunks.append(response.choices[0].text.strip())
    return translated_chunks

# 示例
chunks = ["这是一段测试文本。", "这是另一段测试文本。"]
translations = translate_chunks_to_chinese(chunks)
for i, translation in enumerate(translations):
    print(f'原文: {chunks[i]}')
    print(f'翻译结果: {translation}')




