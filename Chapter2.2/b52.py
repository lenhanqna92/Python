def is_perfect(n: int) -> bool:
    if n < 2:
        return False
    divisors_sum = 1  
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            divisors_sum += i
            if i != n // i:
                divisors_sum += n // i
    return divisors_sum == n


def main():
    print("Perfect numbers from 1 to 10000:")
    for num in range(1, 10001):
        if is_perfect(num):
            print(num)


if __name__ == "__main__":
    main()