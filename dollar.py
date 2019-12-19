import bs4
import requests
# https://finance.naver.com/marketindex/ 이 주소를 통해
# 환율이 얼마인지 가져오는 프로그램을 작성해주세요!

html = requests.get('https://finance.naver.com/marketindex/')
# html에 url주소의 Html파일정보를 가져온다.
# html.txt를 내가 보기 좋고 접근하기 좋게 변경
soup = bs4.BeautifulSoup(html.text,'html.parser')
dollar = soup.select_one('#exchangeList > li.on > a.head.usd > div > span.value')

print (dollar.text)
#exchangeList > li.on > a.head.usd > div > span.value