def selection_sort(A):
    for i in range(0, len(A)-2):
        min = i
        for j in range(i+1, len(A)-1):
            if A[j] < A[min]:
                min = j
        A[i], A[min] = A[min], A[i]
    return A

input = [9, 3, 4, 12, 10, 5, 4, 11]

sorted = selection_sort(input)
print(sorted)