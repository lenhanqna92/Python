def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
if __name__ == "__main__":
    number = int(input("Enter an integer: "))
    if is_prime(number):
        print(f"{number} = prime number.")
    else:
        print(f"{number} != prime number.")
