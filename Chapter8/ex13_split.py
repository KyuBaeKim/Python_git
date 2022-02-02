# 구분자 split --> 리스트로 만듦
# .split
# 구분자를 끊어서 원소로 만든다(tokenizing)
# 하나의 원소를 token이라 부른다.

s = "짜장 짬뽕 탕수육"
print(s.split())

s2 = '서울->대전->대구->부산'
cities = s2.split('->')
print(cities)

for city in cities :
    print(city)