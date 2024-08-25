T = int(input())

for _ in range(T):
    k = int(input())
    n = int(input())
    people = [x for x in range(1, n+1)] # 0층
    
    for i in range(k):
        for j in range(1,n):   
            people[j] += people[j-1]
            
    print(people[-1])

        
        
    
'''
3층: 1 5 15 35 70 ...     
2층: 1 4 10 20 35 ...
1층: 1 3 6 10 15 ...
---------------------
0층: 1 2 3 4 5 ...
'''