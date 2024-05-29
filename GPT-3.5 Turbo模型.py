#GPT-3.5 Turbo 模型.py

#這個程式的功能是使用 OpenAI 的 GPT-3.5 Turbo 模型來進行對話式的文本生成。
#具體來說，它模擬了一個對話情境，使用者可以向程式提供一些對話內容，然後程式將會基於提供的對話內容進行相應的文本生成，並返回結果。
#在這個程式中，它發送了一個 POST 請求到 OpenAI 的 API 端點，並在請求中包含了模型名稱、角色設定以及對話內容等信息。
#然後，OpenAI 的服務端會使用指定的模型來處理這些對話信息，並返回生成的文本結果。最後，程式將返回的結果進行輸出，以供使用者查看生成的文本內容。


import requests
import json

# 设置您的 OpenAI API 密钥
api_key = ""API KEY""


# 定义请求的 URL
url = "https://api.openai.com/v1/chat/completions"

# 定义请求头
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
}

# 定义请求体
data = {
    "model": "gpt-3.5-turbo",
    "messages": [
        {
            "role": "system",
            "content": "You are a helpful assistant."
        },
        {
            "role": "user",
            "content": "Hello!"
        }
    ]
}

# 发送 POST 请求
response = requests.post(url, json=data, headers=headers)

# 获取响应结果
result = response.json()

# 输出结果
print(result)
