# 네이버에 있는 증시 페이지에 대신 접속을 해서 ,
# 현재 코스피 지수를 가져오는 프로그램
# bash에서 pip requests 를 치면 requests 모듈을 다운받고 설치한다.
import random
import requests
import bs4

# 이 주소로 요청을 보내면 응답으로 HTML파일이 도착함.
html = requests.get('ttps://finance.naver.com/sise/sise_index.nhn?code=KOSPI')

# html.text 를 내가 보기 좋게 접근할 수 있게 변경.
soup = bs4.BeautifulSoup(html.text,'html.parser')
# css select_one으로 내가 원하는 태그를 가져오겠다.
kospi = soup.select_one('#now_value')

print(kospi.text)


#오류상황 issue : 파일중 string.py라는 파일이 있어서 requests에서 해당 파일을 인식해서 발생 파일명수정


#now_value