#n, m = map(int, input().split())

#result = 0
#for i in range(n):
    #data = list(map(int, input.split()))
    #min_value = min(data)
    #result = max(result, min_value)

#print(result)

n, m = map(int, input("N과 M 값을 입력하세요: ").split())

result = 0
for i in range(n):
    data = list(map(int, input("각 행의 원소 값을 입력하세요(한줄씩만): ").split()))
    min_value = min(data)
    result = max(result, min_value)

print("결과:", result)
