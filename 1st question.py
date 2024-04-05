1] question 
ans-  it is in python code- 


def merge_sorted_arrays(X, Y):
    # Remove zeros from X and merge Y into it
    k = len(X) - 1
    m, n = len(X), len(Y)

    # Move non-empty elements of X to the beginning
    for i in range(m - 1, -1, -1):
        if X[i] != 0:
            X[k] = X[i]
            k -= 1

    # Merge X and Y
    i, j = k + 1, 0
    while i < m and j < n:
        if X[i] < Y[j]:
            X[k] = X[i]
            i += 1
        else:
            X[k] = Y[j]
            j += 1
        k += 1

    # Copy remaining elements from Y (if any)
    while j < n:
        X[k] = Y[j]
        j += 1
        k += 1

# Example usage
X = [0, 2, 0, 3, 0, 5, 6, 0, 0]
Y = [1, 8, 9, 10, 15]
merge_sorted_arrays(X, Y)

print(X)  # Output: [1, 2, 3, 5, 6, 8, 9, 10, 15]
