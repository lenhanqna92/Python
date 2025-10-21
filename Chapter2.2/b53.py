def all_sublists(lst: list) -> list:
    result = [[]] 
    n = len(lst)
    for i in range(n):
        for j in range(i + 1, n + 1):
            result.append(lst[i:j])
    return result


def main():
    nums = [1, 2, 3,4,5,6,7,8,9,10]
    subs = all_sublists(nums)
    print("All sublists of", nums, "are:")
    for s in subs:
        print(s)


if __name__ == "__main__":
    main()
    