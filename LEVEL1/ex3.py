# 1.리스트
list1 = [1,2,3,4]
list2 = [5,6,7,8]
print(list1[2])
print("="*50)

list3 = list1 + list2
print(list3)


#스칼라 , 벡터(방향이 있는숮자 [1,3,5])
# 2차원 matrix 3차원 tensor
list4 = [list1 , list2]

print(list4)
print("="*50)

list1.append(10)
print(list1)

# list5 = [list1,11]    
# print(list5)

del list1[0]
print(list1)

list6 = list(range(10))
print(list6)

list7 = list(range(1,12))
print(list7)
list7[0] = 100
print(list7)

# 2.튜플 -- 읽기 전용 변수 데이터 변경 불가능
tuple1 = (1,2,3)
print(tuple1)
tuple2 = (4,5,6)
print (tuple1 + tuple2)
tuple3 = (tuple1, tuple2)
print (tuple3)

list10 = list(tuple1)
print(list10)

# 3.딕셔너리


# 소스올리기
# S D:\KISWIRE> git init   ** 초기화는 한번만...
# Initialized empty Git repository in D:/KISWIRE/.git/
# PS D:\KISWIRE> git add .
# PS D:\KISWIRE> git commit -m "1.파이선 변수, 리스트, 튜플"
#  3 files changed, 124 insertions(+)
#  create mode 100644 LEVEL1/ex1.py
#  create mode 100644 LEVEL1/ex2.py
#  create mode 100644 LEVEL1/ex3.py
# PS D:\KISWIRE> git log
# commit b88d21f3a5f6ee8ca14bee6bd1e81f62892a52cd (HEAD -> master)
# Author: ssar@nate.com <ssar@nate.com>
# Date:   Tue May 4 17:46:20 2021 +0900

#     1.파이선 변수, 리스트, 튜플
# PS D:\KISWIRE> git remote add origin https://github.com/GREATSHIN2000/python-study.git
# PS D:\KISWIRE> 

# PS D:\KISWIRE> git push origin master