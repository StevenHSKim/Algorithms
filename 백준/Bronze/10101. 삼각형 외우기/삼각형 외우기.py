angle_1 = int(input())
angle_2 = int(input())
angle_3 = int(input())

if angle_1 + angle_2 + angle_3 == 180:
    if angle_1 == angle_2 == angle_3 == 60:
        print("Equilateral")
    elif angle_1 == angle_2 or angle_1 == angle_3 or angle_2 == angle_3:
        print("Isosceles")
    else:
         print("Scalene")
else:
    print("Error")