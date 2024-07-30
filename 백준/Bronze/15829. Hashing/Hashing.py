L = int(input())
arr = list(input())
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

sum = 0
cnt = 0

for i in arr:
    idx = alphabet.index(i)+1
    sum += idx * (31**cnt)
    cnt += 1
    
print(sum%1234567891)