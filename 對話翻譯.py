# 對話翻譯.py

#這兩個程式在功能上是相似的，都是將給定的英文文本翻譯成中文。它們的主要差異在於使用的 OpenAI API 功能不同。
#在 translate.py 中，使用的是 OpenAI 的对话模型（ChatCompletion），它被用來處理文本轉換的請求，以便讓使用者與模型進行對話式的翻譯。
#而在 text_translation.py 中，則使用的是 OpenAI 的翻譯模型（Translation），它專門用於將文本從一種語言翻譯為另一種語言，不包含與使用者的對話互動。
#因此，雖然兩者都可以用來進行文本翻譯，但是 translate.py 中的對話模型提供了更多與使用者互動的可能性。

import openai

# 设置 OpenAI API 密钥
openai.api_key = "sk-proj-tXsJfPWYz4cI3CLAObzIT3BlbkFJ9POG15DPqqkeEFaNpYR3"

# 定义要翻译的文本
input_text = "Translate the following text into Chinese:\n\nHello, how are you?"

# 使用 OpenAI API 完成翻译
response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",  # 使用聊天模型
    messages=[
        {"role": "system", "content": "Translate the following text into Chinese:"},
        {"role": "user", "content": input_text}
    ],
    temperature=0.7,
    max_tokens=200
)

# 输出翻译结果
print('翻译结果:', response.choices[0].message['content'])


