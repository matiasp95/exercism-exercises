def find_fewest_coins(coins, target):
    min_coins = [target+1] * (target + 1)
    min_coins[0] = 0
    coin_values = [[] for _ in range(target + 1)]
    for coin in coins:
        for i in range(coin, target + 1):
            if min_coins[i - coin] + 1 < min_coins[i]:
                min_coins[i] = min_coins[i - coin] + 1
                coin_values[i] = coin_values[i - coin] + [coin]

    return coin_values[target]
    

                

print(find_fewest_coins([1, 5,6,9],10))


