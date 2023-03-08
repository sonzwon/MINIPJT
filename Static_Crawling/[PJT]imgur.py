import requests as req

url = "https://api.imgur.com/3/image?client_id=546c25a59c58ad7"

with open("img.jpg", "rb") as f:
    img = f.read()

# print(len(img))


res = req.post(url, files={
    "image": img,
    "type": "file",
    "name": "img.jpg"
})
# print(res.status_code)
# print(res.text)

link = res.json()["data"]["link"]
print(link)

html = f"""
<html>
<head>
    <title>방금 업로드한 이미지</title>d
</head>
<body>
    <img src="{link}">
</body>
</html>
"""

with open("img.html", "w") as f:
    f.write(html)