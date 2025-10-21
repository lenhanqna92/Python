def print_five_last() -> None:
    squares = []
    for i in range(1, 21):         
        squares.append(i ** 2)     
    print(squares[-5:])           

print_five_last()