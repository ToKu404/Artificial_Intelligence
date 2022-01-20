def bubble_sort(A):
    for i in range(len(A)-2):

        '''Pada Pseudocde smua perbandingan dibuat bahkan 
        jika array sdh diurutkan. Hal ini meningkatkan 
        waktu eksekusi, Untuk mengecek hal ini dibuatlah
        variabel swapped'''
        swapped = False

        for j in range(len(A)-2-i):
            if A[j+1] < A[j]:
                A[j], A[j+1] = A[j+1], A[j]

                swapped = True

        if not swapped:
            break
    return A

input = [9, 3, 4, 12, 10, 5, 4, 11]

sorted = bubble_sort(input)
print(sorted)