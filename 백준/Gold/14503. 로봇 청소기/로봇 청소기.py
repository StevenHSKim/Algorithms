n,m = map(int, input().split())
r,c,d = map(int, input().split())

room = []
for _ in range(n):
    room.append(list(map(int, input().split())))
    
# 북, 동, 남, 서
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

count = 0

while True:
    # 현재 칸이 청소되지 않은 경우 청소
    if room[r][c] == 0:
        room[r][c] = 2  # 벽이 1이니까, 2로 구분
        count += 1
        
    # 현재 칸 주변 4칸 중 청소 안된 칸 없는지 확인
    found = False # 청소 안 된 칸 발견 못함
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if room[nr][nc] == 0:
            found = True # 청소 안 된 칸 발견
            break

    # 청소 안 된 칸 없는 경우
    if found != True: # if not found
        back_d = (d+2)%4
        br = r + dr[back_d]
        bc = c + dc[back_d]
        if room[br][bc] != 1:
            r,c = br,bc
        else:
            break

    else:
        d = (d+3)%4
        nr = r + dr[d]
        nc = c + dc[d]
        
        if room[nr][nc] == 0:
            r,c = nr, nc

print(count)