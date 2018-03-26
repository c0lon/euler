from functools import lru_cache


@lru_cache()
def is_prime(x):
    if x in (0, 1, 2):
        return True
    if not x % 2:
        return False

    return not bool(factors(x))


@lru_cache()
def factors(x):
    _factors = set()

    for i in range(2, int(x**0.5)+1):
        if not x % i:
            _factors.add(i)
            _factors.add(int(x/i))

    return sorted(list(_factors))


@lru_cache()
def is_palindrome(s):
    if not isinstance(s, str):
        s = str(s)

    if len(s) in (0, 1):
        return True
    elif s[0] == s[-1]:
        return is_palindrome(s[1:-1])
    else:
        return False


if __name__ == '__main__':
    print(is_prime(35))
    print(is_prime(47))
    print(factors(12))
    print([is_prime(i) for i in factors(12)])
