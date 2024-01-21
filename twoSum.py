def two_sum(lst, k):
    seen = {}
    for num in lst:
        if k - num in seen:
            return True
        seen[num] = True
    return False
    
a = [1,3,5,7,8]
b = 10
print(two_sum(a, b))
