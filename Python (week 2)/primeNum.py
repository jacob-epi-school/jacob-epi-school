def is_prime(n):
    if n > 1:
        for i in (2, n):
            if n % i != 0:
                return True
            else:
                return False
    else:
        return False
