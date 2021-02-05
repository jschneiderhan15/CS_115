#Jack Schneiderhan
#Lab 4: Change Maker
#I pledge my honor that I have abided by the Stevens Honor System.

def change(amount, coins):
    '''returns the smallest number of coins needed to make a total'''

    if amount == 0:
        return 0
    elif coins == []:
        return float("inf")
    elif coins[0] > amount:
        return change(amount, coins[1:])
    else:
        use = change(amount - coins[0], coins)
        lose = change(amount, coins[1:])
        if use < lose:
            return 1 + use
        
    return lose
        
