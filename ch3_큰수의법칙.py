n, m, k = map(int, input("N, M, K 값을 입력하세요: ").split())
data = list(map(int, input("각 수열의 원소 값을 입력하세요: ").split()))

data.sort()
first = data[n-1]
second = data[n-2]

count = int(m / (k+1)) * k
count += m % (k+1)

result = 0
result += count * first
result += (m - count) * second

print("결과:", result)
