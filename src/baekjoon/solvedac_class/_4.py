class _15650:
    """N과 M (2)"""
    
    def __init__(self):
        self.n = None
        self.m = None
        
        self.get_input()
    
    def get_input(self):
        self.n, self.m = map(int, input().split(" "))

def _15654():
    n, m = list(map(int, input().split(" ")))
    nums = list(map(int, input().split(" ")))
    
    print(nums)
    
    result = []
    
    for i in range(n-1):
        for j in range(i+1, n):
            result.append(f"{nums[i]} {nums[j]}")
    
    result.sort()
    
    print(result)

_15654()

# 3
# 26 40 83
# 49 60 57
# 13 89 99
# -> 

# 8
# 71 39 44   44
# 32 83 55   32
# 51 37 63   37
# 89 29 100  89
# 83 58 11   11 
# 65 13 15   13
# 47 25 29   25
# 60 66 19   19
# -> 253

# [1, 2, 3, 4]
# 4 -> 4, 5, 6
# 4, 5 -> 5, 6
# 4, 6 -> 6
# 5, 6
# [2, 3, 4, 5]
# [3, 4, 5, 6]

# 6 3

# 1 2 3
# 1 2 4
# 1 2 5
# 1 2 6
# 1 3 4
# 1 3 5
# 1 3 6
# 1 4 5
# 1 4 6
# 1 5 6
# 2 3 4
# 2 3 5
# 2 3 6
# 2 4 5
# 2 4 6
# 2 5 6
# 3 4 5
# 3 4 6
# 3 5 6
# 4 5 6


# _15650()