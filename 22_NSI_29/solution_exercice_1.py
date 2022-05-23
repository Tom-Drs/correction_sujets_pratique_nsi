def fibonacci(n: int) -> int:
    suite = [1, 1]
    for _ in range(n-2):
        suite.append(suite[-1] + suite[-2])
    return suite[-1]


assert fibonacci(1) == 1
assert fibonacci(2) == 1
assert fibonacci(25) == 75025
assert fibonacci(45) == 1134903170
