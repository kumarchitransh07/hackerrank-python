if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    brr = sorted(set(arr))
    print(brr[-2])
