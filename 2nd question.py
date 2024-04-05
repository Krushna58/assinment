def find_max_sum_path(X, Y):
    m, n = len(X), len(Y)
    sum_x, sum_y = 0, 0
    result = 0
    i, j = 0, 0

    while i < m and j < n:
        # Handle duplicate elements in X
        while i < m - 1 and X[i] == X[i + 1]:
            sum_x += X[i]
            i += 1
        # Handle duplicate elements in Y
        while j < n - 1 and Y[j] == Y[j + 1]:
            sum_y += Y[j]
            j += 1

        if X[i] < Y[j]:
            sum_x += X[i]
            i += 1
        elif X[i] > Y[j]:
            sum_y += Y[j]
            j += 1
        else:  # Common element
            result += max(sum_x, sum_y) + X[i]
            i += 1
            j += 1
            sum_x, sum_y = 0, 0

    # Process remaining elements (if any)
    while i < m:
        sum_x += X[i]
        i += 1
    while j < n:
        sum_y += Y[j]
        j += 1

    # Add the maximum of the last sums
    result += max(sum_x, sum_y)
    return result

# Example usage
X = [3, 6, 7, 8, 10, 12, 15, 18, 100]
Y = [1, 2, 3, 5, 7, 9, 10, 11, 15, 16, 18, 25, 50]
print("Maximum sum path:", find_max_sum_path(X, Y))
