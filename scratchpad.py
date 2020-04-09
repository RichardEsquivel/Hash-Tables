# We want to traverse an array with subarrays and get the min value within those arrays and add them all up for a total

# Array a with subarrays we will traverse
a = [[8, 4], [90, -1, 3], [9, 62], [-7, -1, -56, -6], [201], [76, 18]]

# We will iterate through each index and for each will capture the min using the min method and then add those totals


def minArraySums(arr):
    # initialize sum to 0
    sum = 0
# calculate number of elements to to iterate through using range and based on length of array
    n = len(arr)
    for i in range(n):
        sum += min(arr[i])
    return sum


print(minArraySums(a))
