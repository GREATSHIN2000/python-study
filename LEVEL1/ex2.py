# 문자열함수
# find,rfind,join

str1 = "가나-다-라"

# r1 = str1.find('-')
# print (r1)

# r2 = str1.find('-',3)
# print (r2)

# r3 = str1.rfind('-')
# print (r3)

tel1 = '02-2222-7874'
tel2 = '051-777-8373'

t1 =  tel1.find('-') + 1
t2 =  tel1.rfind('-')
print(tel1[t1:t2])

# 가,나,다,라,마
str2 = "가나다라마"
r4 = ",".join(str2)
print (r4)
