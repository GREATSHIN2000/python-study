# 오버로딩 없음 = 편법사용

def add(a, b):
    return a+b


print(add(1, 2))

# 오버로딩 없음 = 편법사용


def minus(a, b=5):
    return a-b


print(minus(10))
print(minus(10, 9))


def many(*data):  # 튜플로 받음
    print(data)


many(1, 2, 3, 4, 5)


def KeyWord(**data):  # 딕셔너리 데이터 받기
    print(data)


KeyWord(id=1, username="SHIN")

n1 = 1


def var_test():
    global n1  # global 을 사용하여 전역변수로 인식
    n1 = 2


var_test()
print(n1)
