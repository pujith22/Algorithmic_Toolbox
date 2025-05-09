# python3


def change_naive(money):
    min_coins = float("inf")

    for num1 in range(money + 1):
        for num3 in range(money // 3 + 1):
            for num4 in range(money // 4 + 1):
                if 1 * num1 + 3 * num3 + 4 * num4 == money:
                    min_coins = min(min_coins, num1 + num3 + num4)

    return min_coins

def change(money):
    dp = [-1]*(money+1)
    return change_helper(money,dp)

def change_helper(money,dp):
    if money==0:
        return 0
    if money<0:
        return float("Inf")
    if money==1 or money==3 or money==4:
        return 1
    if dp[money]!=-1:
        return dp[money]
    dp[money] = 1+min(min(change_helper(money-1,dp),change_helper(money-3,dp)),change_helper(money-4,dp))
    return dp[money]

if __name__ == '__main__':
    amount = int(input())
    print(change(amount))
