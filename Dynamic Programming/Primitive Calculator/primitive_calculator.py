# python3


def compute_operations(n):
    assert 1 <= n <= 10 ** 6
    dp = [float("Inf")]*(n+1)
    dp[1] = 0
    sol = [n]
    operation = [-1,0]
    op = -1
    for i in range(2,n+1):
        if dp[i-1]+1<dp[i]:
            dp[i]=1+dp[i-1]
            op = 0
        if i%2==0 and dp[i//2]+1<dp[i]:
            dp[i] = dp[i//2]+1
            op = 1
        if i%3==0 and dp[i//3]+1<dp[i]:
            dp[i] = dp[i//3]+1
            op = 2
        operation.append(op)
    while n>1:
        if operation[n]==0:
            sol.append(n-1)
            n = n-1
        if operation[n]==1:
            sol.append(n//2)
            n = n//2
        if operation[n]==2:
            sol.append(n//3)
            n = n//3
    sol.reverse()
    return sol


if __name__ == '__main__':
    input_n = int(input())
    output_sequence = compute_operations(input_n)
    print(len(output_sequence) - 1)
    print(*output_sequence)
