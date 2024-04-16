def min_coin_count(change):
    coins = [500, 100, 50, 10]
    count = 0
    for coin in coins:
        count += change // coin
        change %= coin
    return count

def main():
    N = int(input("거슬러줘야 하는 돈을 입력하세요: "))
    if N % 10 != 0:
        print("거슬러줘야 하는 돈은 항상 10의 배수여야 합니다.")
        return
    result = min_coin_count(N)
    print("거슬러줘야 하는 동전의 최소 개수:", result)

if __name__ == "__main__":
    main()
