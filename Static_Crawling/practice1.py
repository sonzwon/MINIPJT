from bs4 import BeautifulSoup as BS
import requests as req

url = "https://search.shopping.naver.com/search/all?query=%EC%95%84%EC%9D%B4%ED%8F%B0%20%EC%BC%80%EC%9D%B4%EC%8A%A4&cat_id=&frm=NVSHATC"
res = req.get(url)
soup = BS(res.text, "html.parser")


arr = soup.select("div.list_basis div>a:first-child[title]")
for a in arr:
    print(a.get_text(strip=True))
