input = [9, 3, 4, 12, 10, 5, 4, 11]

def insertionSort(A):
    for j in range(1,len(A)):
        key = A[j] 
        # Insert A[j] into sorted sequence A[1..j-1]
        i = j-1
        while (i>=0 and A[i]>key):
            A[i+1] = A[i]
            i = i - 1
        A[i+1] = key
    return A

sorted = insertionSort(input)
print(sorted)