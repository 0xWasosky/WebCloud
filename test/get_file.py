import requests


url = "http://127.0.0.1:8080/getfile"
payload = {'file': 'a3f359d1d5de4580358fbf58c9c322eb3a3544bd6d5ca085', 'key': 'L8qfO-rm5rZt83U3XueQLWwvkmrKq3Y_6J49z60RZVmKKC5-amQr3rNglXVwbUtUvSrwwcv89qyWWFpklr3p5An5kLnrh9tgxR5YCtFpSswn9OijvJ0M6OqT5AMA6myY_OhAEn2FSortUVUJ0Ba9rmtA4Q=='}

response = requests.post(url, json=payload)


with open("result.txt", 'wb') as f:
    f.write(response.content)
