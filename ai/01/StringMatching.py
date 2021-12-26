def string_matching(T, P):
    for i in range(len(T)-len(P)):
        j = 0
        while j<len(P) and P[j] == T[i+j]:
            j += 1
        if j == len(P):
            return i
    return -1

text = "indonesia tanah airku"
pattern = "tanah"

result = string_matching(text, pattern)
print("Pattern ditemukan pada index ke",result if result!=-1 else "Tidak Ditemukan")