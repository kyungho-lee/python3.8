import requests
import bs4

html = requests.get('https://www.naver.com')
soup = bs4.BeautifulSoup(html.text,'html.parser') # 규칙 

keywords = soup.select('span.ah_k') # 값이 여러개 일때 배열로 저장됨, 

#keywords = ['a','b','c']
# for keywords in keywords:
#     print(keywords.text)

# 배열[0:n]  → 배열의 0번째 인덱스 부터 n-1번째
# 인덱스들의 요소를 가져와서 배열로 만든다.

real_keywords = keywords[0:20]  # keywords 배열에서 0~20까지만 저장

# real_keywords에 있는 배열요소에 keyword라고 인덱스를 붙이고 keyword에 있는
# 문자만 real_real_keywords에 배열로 저장
real_real_keywords = [keyword.text for keyword in real_keywords] 

# 무엇이 1등인지 모르게 가나다 순으로 정렬해버리기
problem = sorted(real_real_keywords)
print('아래의 보기 중에서 1위를 고르세요')
print(problem)

# 사용자 입력받기
answer = input('당신이 생각한 실시간 검색어 1위는? : ')
# 사용자 입력 예외처리 공백없애기
answer = str.replace(answer,' ','')
# 배열[0] : 배열의 첫번째 요소
# == 양쪽 변수에 값이 같은지 확인  : 배열첫번째 값과 비교
if answer == real_real_keywords[0] :   
    print(f'당신이 입력한 답 :{answer} ')
    print('정답입니다.')
else:
    print(f'당신이 입력한 답 :{answer} ')
    print('오답입니다.')





# [0,1,2,3,4,5............,100]
# numbers = [i for i in range(0,101)]  #numbers 라는 
# print(numbers)

# numbers = []
# for i in range(0,101):
#     numbers.append(i)
# print(numbers)

