import requests

res = requests.get("https://zipcloud.ibsnet.co.jp/api/search?zipcode=7830060")

# print(res.text["status"])
json = res.json()
print(json()["results"][0]["prefcode"])
