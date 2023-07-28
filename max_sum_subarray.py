# Kadane's Algorithm (Medium)
# Given an array Arr[] of N integers. Find the contiguous sub-array(containing at least one number) 
# which has the maximum sum and return its sum.

# Example 1:

# Input:
# N = 5
# Arr[] = {1,2,3,-2,5}
# Output: 9

 

# Example 2:

# Input:
# N = 4
# Arr[] = {-1,-2,-3,-4}
# Output:
# -1

def get_max_sum(arr, n):
    curr_max = arr[0]
    abs_max = arr[0]

    for i in range(1, n):
        curr_max = max(curr_max + arr[i], arr[i])
        abs_max = max(curr_max, abs_max)

    return abs_max

print(get_max_sum([1, 2, 3, -2, 5], 5))  # Output: 9
print(get_max_sum([-1, -2, -3, -4], 4))  # Output: -1