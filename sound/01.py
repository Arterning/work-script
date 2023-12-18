import requests
api_secret_key = "1dd04d5de3cf467087a24ed77814ec9e"  # your api_secret_key
# 禁用SSL证书验证
requests.packages.urllib3.disable_warnings()

url = 'https://lm_experience.sensetime.com/v1/nlp/chat/completions'
data = {
    "messages": [{"role": "user", "content": "Say this is a test!"}],
    "temperature": 0.8,
    "top_p": 0.7,
    "max_new_tokens": 1024,
    "repetition_penalty": 1.05,
    "stream": True,
    "user": "test"
}
headers = {
    'Content-Type': 'application/json',
    'Authorization': api_secret_key
}

response = requests.post(url, headers=headers, json=data, stream=True, verify=False)
for chunk in response.iter_lines():
    print(chunk)