def solution(answers):
    answer = []
    
    student1 = [1,2,3,4,5]
    student2 = [2,1,2,3,2,4,2,5]
    student3 = [3,3,1,1,2,2,4,4,5,5]
    score = [0,0,0]
    
    for i, num in enumerate(answers):
        if num == student1[i % len(student1)]:
            score[0] += 1
        if num == student2[i % len(student2)]:
            score[1] += 1
        if num == student3[i % len(student3)]:
            score[2] += 1
        
    for i, s in enumerate(score):
        if s == max(score):
            answer.append(i+1)
    
    return answer