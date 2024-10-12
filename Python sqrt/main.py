import math

N = int(input())
# s_a = list(map(int, input().split()))
# s_b = list(map(int, input().split()))
s_a = []
s_b = []

for _ in range(N):
  a, b = map(int , input().split())
  s_a.append(a)
  s_b.append(b)

C = 0

number = (s_a[0] - 0) ** 2 + (s_a[1] - 0) ** 2
sqrt_value = math.sqrt(number)
C += sqrt_value

num_last =  (s_b[-2] - 0) ** 2  + (s_b[-1] - 0) ** 2
sqrt_value = math.sqrt(num_last)
C += sqrt_value


for i in range(N - 1):
  # num = ((((s_a[i])　** 2) - ((s_a[i + 1])) ** 2)) + (((s_b[i]) - (s_b[i + 1])) ** 2) 
  num = ((s_a[i]) - (s_b[i])) ** 2 + (s_a[i + 1] - s_b[i + 1]) ** 2
  sqrt_value = math.sqrt(num)
  C += sqrt_value

print(C)