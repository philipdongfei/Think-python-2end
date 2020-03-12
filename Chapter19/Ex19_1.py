trials = {0:0}
successes = {0:1}
def binomial_coeff(n, k):
    """
    Compute the binomial coefficient "n choose k".
    n: number of trials
    k: number of successes

    returns: int
    """
    '''

    if k == 0:
        return 1
    if n == 0:
        return 0
    '''
    C = [0 for i in range(k+1)]
    C[0] = 1

    for i in range(1, n+1):
        j = min(i, k)
        while (j > 0):
            C[j] = C[j] + C[j-1]
            j -= 1

    return C[k]

