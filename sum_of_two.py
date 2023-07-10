# Sum of two values
# Given an array of integers and a value, 
# determine if there are any two integers in the array whose sum is equal to the given value. 
# Return true if the sum exists and return false if it does not.

# Example:
# Given nums = [2, 7, 11, 15], target = 9,
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].

def find_sum_of_two(arr, target_value):
    visited_elements = set()
    for element in arr:
        if target_value - element in visited_elements:
            return True
        visited_elements.add(element)
    return False

def main():
    v = [5, 7, 1, 2, 8, 4, 3]
    test = [3, 20, 1, 2, 7]

    for i in range(len(test)):
        output = find_sum_of_two(v, test[i])
        print("find_sum_of_two(v, " + str(test[i]) + ") = " + str(output))


main()