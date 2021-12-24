import math

input = [9, 3, 4, 12, 10, 5, 4, 11]

def merge(A, p, q, r):
    n1 = q - p + 1
    n2 = r - q

   
    L = []
    R = []


    for i in range(0, n1-2):
        L[i] = A[p]
        print()
    
    # for j in range(0, n2):
    #     R[j] = A[q+j]
    
    # L[n1+1] = math.inf
    # R[n2+1] = math.inf

    # i = 0
    # j = 0

    # for k in range(p, r):
    #     if L[i] <= R[j]:
    #         A[k] = L[i]
    #         i = i + 1
    #     else:
    #         [k] = R[j]
    #         j = j+1
    
    # return A



def merge_sort(A, p, r):
    if p < r :
        q = math.floor((p+r)/2)
        merge_sort(A, p, q)
        merge_sort(A, q+1, r)
        merge(A, p, q, r)
    
    # print(A)

merge_sort(input, 0, len(input))
    
