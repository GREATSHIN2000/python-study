# 모듈:변수, 함수, 클래스를 모아둔 파일
# 패키지 : 여러 모듈을 하나의 디렉토리로 모아둔건

# built-in 된 모듈  -- print 함수등
# from 패키지 import 모듈
# from 모듈 import 변수,함수,클래스
from hello import Say_hello
# from hello import *
import hello as h
import hello
import sys


print(sys.modules)  # 기본설치되어 있는 모듈
print("="*50)
print(sys.path)  # 새로 설치한 모듈


hello.Say_hello()
h.Say_hello()
Say_hello()
