#HelloWorld 파스칼표기법
#helloWorld 낙타표기법
#hello_world 언더스코어(파이선)

# 타입 추론
#모든것이 오브젝트
#모든것이 인터프리터
# 단축키 ctrl+b  
# ctrl + /  : 주석
# shigt + ctrl + down : 현재행 아래로 복사
# 1. 숫자
a=1
b=1.2
c=4e5

# print(a)
# print(b)
# print(c)
# print(a+b)

# print(type(a))
# print(type(a+c))
# print(type(a+b))

# 연산자
e=3
f=32
# print(e**f)   #제곱
# print(f//e)   #몫
# print(f%e)    #나머지

# 문자열
# "",'' 구분안함
s1 = "안녕하세요"
s2 = '안녕하세요'
s3 = '''
안녕 
'''
s4 = s1+s3
# print (s4)

s5 = '홍길동'
# print (s5 + '님 안녕하세요')
# print(f"{s5}님 안녕하세요")
# print("="*50)

# 3 슬라이싱 연산자
str1 = "가나다라마"

print(str1[0])
print(str1[0:3])
print(str1[-1])
print(str1[1:])

a= 9989.01
print(f"{a:,}")
