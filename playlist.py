T = int(input())  # Number of test cases

for _ in range(T):
    N, X = map(int, input().split())  # Read N and X
    print(N // (3 * X))  # Number of times song C is played completely
