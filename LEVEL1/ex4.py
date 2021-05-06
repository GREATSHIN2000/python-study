# 딕셔너리 {key:value}   ex {1:"홍길동"}   자료:자료           => 파이썬에서 몽고DB 값 넣을때 사용
# 자바스크립트 {key:value}   ex{UserName:"홍길동"}  변수:자료  => 몽고DB (자바스크립트 오브젝트를 넣어야함)
# Json {"Key":Value}   "변수":자료
dic1 = {"username": "SHIN"}
print(dic1)
print("1="*50)

# 딕셔너리 값 찾기
print(dic1["username"])
print("="*50)

# 딕셔너리 값 추가
dic1["password"] = '12345'
print(dic1)
print("="*50)

# 딕셔너리 삭제 (알아서 검색 해보기)

# Key 값 추출
dic2 = {'username': 'SHIN', 'password': '12345'}

print(dic2.keys())
print(dic2.values())
print("="*50)

# 키 값 벨류값 동시 추출
for i in dic2:
    print(i)

print("="*50)

for i in dic2.items():
    print(i)
print("="*50)

list1 = []
for k, v in dic2.items():
    print(k, v)
    list1.append(v)

print("="*50)
print(list1)
