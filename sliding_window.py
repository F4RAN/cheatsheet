def max_sum_subarray(arr, k):
    n = len(arr)
    if n < k:
        return None  # Not enough elements

    # Compute the sum of the first window
    max_sum = sum(arr[:k]) # 2 1 5 = 8
    current_sum = max_sum

    # Slide the window
    for i in range(k, n):
        print(i)             #       Add last item and sub first item ==> slide the window
        current_sum += arr[i] - arr[i - k] # 8 + (a[3] - a[3 - 3])
        max_sum = max(max_sum, current_sum)

    return max_sum

# Example usage
arr = [2, 1, 5, 1, 3, 2]
k = 3
result = max_sum_subarray(arr, k)
print(f"Maximum sum of {k} consecutive elements is: {result}")
