```bash
curl https://lm_experience.sensetime.com/v1/nlp/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: 1dd04d5de3cf467087a24ed77814ec9e" \
  -d '{
        "messages": [{"role": "user", "content": "Say this is a test!"}],
        "temperature": 0.8,
        "top_p": 0.7,
        "max_new_tokens": 1024,
        "repetition_penalty": 1.05,
        "stream": false,
        "user": "test"
  }'
```


```bash
curl https://lm_experience.sensetime.com/v1/nlp/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: 1dd04d5de3cf467087a24ed77814ec9e" \
  -d '{
        "messages": [{"role": "user", "content": "Say this is a test!"}],
        "temperature": 0.8,
        "top_p": 0.7,
        "max_new_tokens": 1024,
        "repetition_penalty": 1.05,
        "stream": false,
        "user": "test"
  }'
```
