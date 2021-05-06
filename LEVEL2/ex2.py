# 클래스

class User:
    username = 'SHIN'
    password = '1234'


u = User()
print(u.username)
print('='*50)


class Persion:
    def __init__(self, username, password):  # 생성자 키워드(self 필수) ==  전역변수에 사용
        self.username = username
        self.password = password
        self.hello = '미리 변수선언 없이 바로 생성'


p = Persion("SHIN", "2345")
print(p.username)
