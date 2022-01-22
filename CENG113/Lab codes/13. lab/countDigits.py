def countDigitsUpto(n, k):
    def countDigits(n,k):
        if n == 0:
            return 0
        else:
            if n % 10 == k:
                return 1 + countDigits(n // 10, k)
            else:  
                return 1 + countDigits(n // 10, k)
    
    if n == 0:
        if k == 0:
            return 1
        else:
            return 0
    else:
        return countDigits(n, k) + countDigitsUpto(n-1, k)