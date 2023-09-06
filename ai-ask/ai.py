import sensenova
import json
import sys
import http.client
import requests

sensenova.access_key_id = "2SmbDQgyHVwMEqVGXxII5McLGlQ"
sensenova.secret_access_key = "CY7gTHeHTPNfADlGyXpZ2GhG1F0UdYG5"

if len(sys.argv) < 3:
    print("请输入咨询的问题，以及确定是否开始新的会话（1-是、0-否）")
    sys.exit()

# 生成会话
if sys.argv[2]=="1":
    conn = http.client.HTTPSConnection("api.sensenova.cn")
    payload = json.dumps({
      "system_prompt": [
        {
          "content": "水稻",
          "role": "user"
        }
      ],
    })
    headers = {
      'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiIyU21iRFFneUhWd01FcVZHWHhJSTVNY0xHbFEiLCJleHAiOjE2OTc2NzQ3NTcsIm5iZiI6MTY4OTg5ODc1Mn0.xL0tvLISfj1xim53flSPQ3VZG572_5UgBqsg8RvQxqo',
      'Content-Type': 'application/json'
    }
    conn.request("POST", "/v1/llm/chat/sessions", payload, headers)
    res = conn.getresponse()
    data = json.loads(res.read().decode("utf-8"))
    file = open('./session_id.txt', 'w')
    file.write(data["session_id"])
    file.close()

# 获取会话
session_id = "";
with open('session_id.txt', 'r') as file:
    session_id = file.readline()
# print(session_id)

# 会话对话
stream = True # 流式输出或非流式输出
model_id = "nova-ptc-xl-v1" # 填写真实的模型ID
payload = json.dumps({
  "know_ids": [
    "sa63b1ee0ac47458d82b60f9b7c32f777"
  ],
  "max_new_tokens": 1024,
  "action": "next",
  "session_id": session_id,
  "content": sys.argv[1],
  "model": model_id,
  "repetition_penalty": 1.05,
  "stream": stream,
  "temperature": 0.01,
  "top_p": 0.7,
  "user": "string"
})
headers = {
  'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiIyU21iRFFneUhWd01FcVZHWHhJSTVNY0xHbFEiLCJleHAiOjE2OTc2NzQ3NTcsIm5iZiI6MTY4OTg5ODc1Mn0.xL0tvLISfj1xim53flSPQ3VZG572_5UgBqsg8RvQxqo',
  'Content-Type': 'application/json'
}
# conn = http.client.HTTPSConnection("api.sensenova.cn")
# conn.request("POST", "/v1/llm/chat-conversations", payload, headers)
# res = conn.getresponse()
# resp = json.loads(res.read().decode("utf-8"))
# print(resp["data"]["message"])

url='https://api.sensenova.cn/v1/llm/chat-conversations'
resp = requests.post(url, headers=headers, data=payload, stream=True)
for chunk in resp.iter_content(chunk_size=1024):
    res = chunk.decode("utf-8").replace('data:','').split('\n\n')
    for part in res:
        if part == '[DONE]':
            sys.stdout.write(part)
        else:
            if len(part) > 1:
                data = json.loads(part)
                delta = data["data"]["delta"]
                sys.stdout.write(delta)
        sys.stdout.flush()