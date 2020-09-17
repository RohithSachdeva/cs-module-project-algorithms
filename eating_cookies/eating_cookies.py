'''
Input: an integer
Returns: an integer
'''

#Replaced my ON^3 solution from support hours with lecture example this morning.

def eating_cookies(n, cache=None):
    # what are our base cases?
    if n < 0:
        return 0
    # this represents there being a number of cookies where we can just take
    # that many cookies
    elif n == 0:
        return 1
    # check the cache to see if the answer is stored in there
    elif cache and cache[n] > 0:
        return cache[n]
    else:
        if not cache:
            # init an empty cache
            cache = {i: 0 for i in range(n+1)}
        # store answers in our cache
        cache[n] = eating_cookies(
            n - 1, cache) + eating_cookies(n - 2, cache) + eating_cookies(n - 3, cache)
    return cache[n]


if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 7

    print(
        f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
