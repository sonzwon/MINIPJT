"""
[[정규식 파싱]]
() : 캡쳐
[] : 이 중 아무거나
. : 아무거나
* : 0개 이상
+ : 1개 이상
? : 없을 수도
\ : 위 특수 기호 무효화
"""

# import re
# s = "hi"
# #print(re.match(r'h.',s)) #<re.Match object; span=(0, 2), match='hi'>
# #print(re.match(r'hi1*',s)) #<re.Match object; span=(0, 2), match='hi'>
# #print(re.match(r'hi1+',s)) # None

# s1 = "color"
# #print(re.match(r'colour', s1)) #None
# #print(re.match(r'colou?r', s1)) #<re.Match object; span=(0, 5), match='color'>

# s2 = "How are you?"
# #print(re.match(r'How are you?', s2)) #<re.Match object; span=(0, 11), match='How are you'>
# #print(re.match(r'How are you\?', s2)) #<re.Match object; span=(0, 12), match='How are you?'>

# s3 = "이 영화는 A등급입니다."
# s3_1 = "이 영화는 C등급입니다."
# s3_2 = "이 영화는 F등급입니다."
# #print(re.match(r'이 영화는 [ABCD]등급입니다.', s3))
# #print(re.match(r'이 영화는 [ABCD]등급입니다.', s3_1))
# #print(re.match(r'이 영화는 [ABCD]등급입니다.', s3_2))
# #<re.Match object; span=(0, 13), match='이 영화는 A등급입니다.'>
# #<re.Match object; span=(0, 13), match='이 영화는 C등급입니다.'>
# #None
# #print(s3.split('이 영화는')[1].split('등급')[0])
# print(re.findall(r'이 영화는 (...)입니다.', s3))

import requests as req
import re

url = "https://finance.naver.com/marketindex/?tabSel=exchange#tab_section"

res = req.get(url)
body = res.text

#정규표현식 준비
r = re.compile(r'h_lst.*?blind">(.*?)</.*?value">(.*?)</', re.DOTALL)
cap = r.findall(body)
# print(cap)


print("-----------------------------")
print("-------------환율--------------")
print("------------------------------")

count = 0
for c in cap:
    count+=1
    print(f"{count}. {c[0]} : {c[1]}")

print("------------------------------")

ctr = int(input("Q) 번호를 선택해주세요\n >>>"))
for c in range(12):
    if c == ctr:
        cm = float(cap[c][1].replace(",",""))
        money = int(input("Q) 환전할 금액을 입력해주세요\n >>>"))
        result = int(money / cm)
        print(f"환전금액 : {result}(달러/엔)")

    
