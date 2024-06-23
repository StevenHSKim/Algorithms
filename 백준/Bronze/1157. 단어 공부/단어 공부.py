word = input().lower()
word_list = list(set(word))
cnt = [] # cnt는 word_list의 원소에 맞추어 count함

for i in word_list:
    count = word.count(i)
    cnt.append(count)
    
if cnt.count(max(cnt)) >= 2:
    print("?")
else:
    print(word_list[cnt.index(max(cnt))].upper())