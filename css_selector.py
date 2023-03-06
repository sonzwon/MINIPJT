"""
[[ CRAWLING BY USING CSS_SELECTOR ]]
CSS; Cascading Style Sheets
"""

from bs4 import BeautifulSoup as BS
import requests as req

url = "https://finance.naver.com/marketindex/exchangeList.naver"
res = req.get(url)
soup = BS(res.text, "html.parser")

tds = soup.find_all("td")

names = []
for td in soup.select("td.tit"):
    names.append(td.get_text(strip=True))

prices = []
for td in soup.select("td.sale"):
    prices.append(td.get_text(strip=True))

# print(names)
# print(prices)


"""
< 한정자 >
* : 모든 노드들
div,p : div노드들과 p노드들
div p : div 안에 있는 p노드들
div>p : div 바로 안에 있는 p노드들
div~p : p옆(앞)에 있는 div노드들
div+p : div 옆(앞)에 있는 p노드들 

< 고급한정자 >
:enabled : 활성화된 상태
:disabled : 비활성화된 상태
:checked : 체크된 상태
:empty : 값이 비어 있는 상태
:first-child : 첫번째 자식 노드
:last-childe : 마지막 자식 노드
:first-of-type : 해당 타입의 첫번째 노드
:last-of-type : 해당 타입의 마지막 노드
:hover : 마우스가 올라간 상태
:not : 다음 조건이 거짓일 경우
:nth-child : n번째 자식 노드
:nth-of-type : n번째 타입
"""

from bs4 import BeautifulSoup as BS

html = """
<html>
    <body>
        <h1>RESERVATION</h1>
        <div>
            <label>예약날짜</label>
            <div><input type="date"></div>
            <label>인원 수</label>
            <div><input type="number"></div>
            <label>예약자</label>
            <div><input type="text"></div>
            <label>휴대폰 번호</label>
            <div><input type="tel"></div>
        </div>
        <br>
        <div>
            <input type="checkbox" checked>
            <span>(필수) 개인정보 처리방침 동의</span>
            <br>
            <input type="checkbox" checked>
            <span>(필수) 서비스 이용약관 동의</span>
            <br>
            <input type="checkbox">
            <span>(선택) 마케팅 수신 동의</span>
        </div>
        <br>
        <input type="submit" value="예약하기">
    </body>
</html>
"""
soup = BS(html, "html.parser")

# # arr = soup.select("input:enabled")
# print(arr)
# # arr = soup.select("input:checked")
# print(arr)
# # arr = soup.select("input:disabled")
# print(arr)
# # arr = soup.select("input:empty")
# print(arr)