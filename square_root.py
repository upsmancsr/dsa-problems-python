# Given an integer x, find the square root of x. 
# If x is not a perfect square, then return floor(√x).

def find_sqr_root(x):
    if x == 0 or x == 1:
        return x
    start = 1
    end = x
    while start <= end:
        mid = (start + end) // 2
        if mid * mid == x:
            return mid
        if mid * mid < x:
            start = mid + 1
            ans = mid   # if sqr root is b/w current mid and mid + 1, then floor with be current mid
        else:
            end = mid - 1

    return ans

print(find_sqr_root(11))
