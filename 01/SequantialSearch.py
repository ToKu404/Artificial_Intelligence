
def sequantial_search(A, K):
    i = 0
    while A[i] != K :
        i += 1
    if i < len(A):
        return i
    else :
        return -1

input = [9, 3, 4, 12, 10, 5, 4, 11]

result = sequantial_search(input, 10)
print("Ditemukan pada index ke",result if result!=-1 else "Tidak Ditemukan")