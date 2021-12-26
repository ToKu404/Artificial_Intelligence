input = [9, 3, 4, 12, 10, 5, 4, 11]

def mergeSort(A):
    if len(A) > 1:
        n = len(A)//2
        leftA = A[:n]
        rightA = A[n:]

        mergeSort(leftA)
        mergeSort(rightA)

        i = j = k = 0

        while i < len(leftA) and j < len(rightA):
            if leftA[i] < rightA[j]:
                A[k] = leftA[i]
                i += 1
            else:
                A[k] = rightA[j]
                j += 1
            k += 1

        while i < len(leftA):
            A[k] = leftA[i]
            i += 1
            k += 1

        while j < len(rightA):
            A[k] = rightA[j]
            j += 1
            k += 1

    return A

sorted = mergeSort(input)
print(sorted)
