import sys

a,b,c,e,d = map(int, sys.stdin.readline().split())

l2 = a**2 + b**2 + c**2 + d**2 + e**2

print(l2%10)