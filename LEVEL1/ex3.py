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