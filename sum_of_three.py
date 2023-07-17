def find_triplet(arr, value):
    arr.sort()
    for i in range(len(arr) - 2): # we subtract 2 because we will have two other pointers 
        left_pointer, right_pointer = i + 1, len(arr) - 1
        while left_pointer < right_pointer:
            current_sum = arr[i] + arr[left_pointer] + arr[right_pointer]
            if current_sum == value:
                return True
            elif current_sum < value:
                left_pointer += 1
            else: # current_sum > value
                right_pointer -= 1
    return False

print(find_triplet([1, 2, 3, 4, 5], 10)) # Output: True
print(find_triplet([2, 4, 5, 6, 9], 22)) # Output: False
