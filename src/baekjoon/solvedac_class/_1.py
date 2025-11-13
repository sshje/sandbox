def _1330():
    """두 수 비교하기"""
    a, b = map(int, input().split(" "))
    if a > b:
        print(">")
    elif a < b:
        print("<")
    else:
        print("==")

def _2438():
    """별 찍기 - 1"""
    n = int(input())
    for i in range(n):
        print("*" * (i + 1))

def _2475():
    """검증수"""
    numbers = map(int, input().split(" "))
    parity = sum([n ** 2 for n in numbers]) % 10
    print(parity)

def _2739():
    """구구단"""
    def multiply(x, y):
        print(f"{x} * {y} = {x * y}")
    
    x = int(input())
    
    for y in range(1, 10):
        multiply(x, y)

def _2741():
    """N 찍기"""
    n = int(input())
    for i in range(n):
        print(i + 1)

_2741()