import requests as req
# [[ webhook ]]

url = "https://webhook.site/f60fa849-c3af-4fb1-b6be-a0d91cd9ca90?name=hi_jiwon"
headers = {"User-Agent":"practice/1"}
# res = req.get(url, headers=headers)
# print(res.text)

res1 = req.post(url, data={
    "name" : "hi"
})
print(res1.text)