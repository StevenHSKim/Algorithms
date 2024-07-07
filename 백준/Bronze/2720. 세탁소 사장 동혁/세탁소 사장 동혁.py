T = int(input())

for _ in range(T):
    C = int(input())
    
    quarter_count = C // 25
    C %= 25
    
    dime_count = C // 10
    C %= 10
    
    nickel_count = C // 5
    C %= 5
    
    penny_count = C // 1
    C %= 1
    
    print(f"{quarter_count} {dime_count} {nickel_count} {penny_count}")