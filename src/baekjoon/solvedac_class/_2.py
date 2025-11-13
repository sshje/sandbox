# 웰컴 키트: https://www.acmicpc.net/problem/30802
def _30802():
    from math import ceil
    # n: 참가자 수
    # sizes: 사이즈별 참가자 수 리스트 (합치면 n)
    # t: 티셔츠 한묶음당 개수
    # p: 펜 한묶음당 개수
    n = int(input())
    sizes = list(map(int, input().split()))
    t, p = map(int, input().split())

    t_bundle = sum(ceil(size / t) for size in sizes)
    p_bundle = n // p
    p_single = n % p

    print(t_bundle)
    print(p_bundle, p_single)


# 스택: https://www.acmicpc.net/problem/10828
def _10828():
    def operate(stack: list[int], cmd: str) -> None:
        match cmd.split()[0]:
            case "push":
                stack.append(int(cmd.split()[1]))
            case "pop":
                print(stack.pop() if stack else -1)
            case "size":
                print(len(stack))
            case "empty":
                print(0 if stack else 1)
            case "top":
                print(stack[-1] if stack else -1)
            case _:
                pass

    n = int(input())
    stack = []

    for _ in range(n):
        cmd = input().strip()
        operate(stack, cmd)


# 큐: https://www.acmicpc.net/problem/10845
def _10845():
    # https://docs.python.org/ko/3.13/library/collections.html#collections.deque
    from collections import deque
    
    def operate(q: deque, cmd: str) -> None:
        match cmd.split()[0]:
            case "push":
                q.append(int(cmd.split()[1]))
            case "pop":
                print(q.popleft() if q else -1)
            case "size":
                print(len(q))
            case "empty":
                print(0 if q else 1)
            case "front":
                print(q[0] if q else -1)
            case "back":
                print(q[-1] if q else -1)
            case _:
                pass
    
    n = int(input().strip())
    q = deque()
    
    for _ in range(n):
        cmd = input().strip()
        operate(q, cmd)


if __name__ == "__main__":
    _10845()