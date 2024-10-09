def solution(bandage, health, attacks):
    max_health = health
    continuous = 0
    
    for i in range(1, attacks[-1][0]+1):
        skip = False
        
        for j in attacks:
            if i == j[0]:
                health -= j[1]
                
                if health <= 0:
                    return -1
                
                continuous = 0
                skip = True
                
        if skip:
            continue
        
        health += bandage[1]
        continuous += 1
        
        if continuous == bandage[0]:
            health += bandage[2]
            continuous = 0
        
        if health > max_health:
            health = max_health        
        

    
    return health