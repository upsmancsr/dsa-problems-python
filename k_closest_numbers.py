# Find k closest numbers
# Given a sorted number array and two integers ‘K’ and ‘X’, 
# find ‘K’ closest numbers to ‘X’ in the array. 
# Return the numbers in the sorted order. ‘X’ is not necessarily present in the array.

# Example:
# Input: arr = [1,2,3,4,5], k = 4, x = 3
# Output: [1,2,3,4]

# Input: [2, 4, 5, 6, 9], k = 3, x = 6
# Output: [4, 5, 6]

def find_k_closest_nums(arr, k, x):
    closest_index = binary_search(arr, x)    # find index of the value closest to target value
    left_pointer = closest_index -1
    right_pointer = closest_index
    n = len(arr)
    while right_pointer - left_pointer - 1 < k:
        # if both pointers are in range:
        if left_pointer >= 0 and right_pointer < n:
            diff_left = abs(arr[left_pointer] - x)    # calulate diff between target value and left_pointer value
            diff_right = abs(arr[right_pointer] - x)   # calculate diff between target value and right_pointer value
            if diff_left <= diff_right:               # if left value is closer to target than right value
                left_pointer -= 1
            else:                                     # else if right value is closer
                right_pointer += 1
        # if right_pointer is out of range but left is still in range:
        elif left_pointer >= 0:
            left_pointer -= 1
        # if left_pointer is out of range but right is still in range:
        elif right_pointer < n:
            right_pointer += 1
    # now return values across range k, closest values to target:
    return arr[left_pointer +1: right_pointer]

def binary_search(arr, target):
    low_index = 0
    high_index = len(arr) - 1
    while low_index <= high_index:
        mid_index = low_index + (high_index - low_index) // 2    # calulate index in middle of low and high
        if arr[mid_index] == target:                             # if the target is at mid_index, return mid_index
            return mid_index
        elif arr[mid_index] < target:                            # if mid_index value is less that the target reset low_index to one higher than mid
            low_index = mid_index + 1
        else:
            high_index = mid_index - 1                           # otherwise reset high_index to one less than mid
    
    # At this point low_index must be greater than high_index, they have crossed
    # So I need to know whether the low_index value or the high_index value is closer to the target value
    # And if the low_index is greater than the length of the array, then there's no value there
    # so the closer value must the high_index value (remember again that the indeces have crossed)
    if low_index < len(arr) and abs(arr[low_index] - target) < abs(arr[high_index] - target):
        return low_index
    return high_index

def main():
    print(find_k_closest_nums([1, 2, 3, 4, 5], 4, 3))  # Output: [1, 2, 3, 4]
    print(find_k_closest_nums([2, 4, 5, 6, 9], 3, 6))  # Output: [4, 5, 6]

main()
