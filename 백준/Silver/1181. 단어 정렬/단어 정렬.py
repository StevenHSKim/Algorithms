N = int(input())
arr = []

for i in range(N):
    arr.append(input())

# 중복값 제거
set_arr = set(arr)
arr = list(set_arr) 

arr.sort()        # 그냥 sort() 하면 알파벳 순으로 정렬
arr.sort(key=len) # 그 다음 길이대로 정렬

for i in arr:
    print(i)
     