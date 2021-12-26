# ALGRORITMA DAN STRUKTUR DATA

## A. FUNDAMENTAL ALGORITMA

​	**Algoritma** adalah prosedur komputasi yang terdefinisi dengan baik yang mengambil beberapa nilai, atau seperangkat nilai, sebagai **input** dan menghasilkan beberapa nilai, atau seperangkat nilai sebagai **output.** Algoritma merupakan urutan langkah-langkah komputasi yang mengubah input ke dalam output. Algotima juga dapat dilihat sebagai alat untuk **memecahkan masalah komputasi** yang ditentukan dengan baik.

Algoritma dikatakan **true** jika, untuk setiap contoh input, itu berhenti dengan output yang benar. Algoritma yang benar memecahkan masalah komputasi yang diberikan. Algoritma yang **false** mungkin tidak berhenti sama sekali pada beberapa contoh input atau mungkin berhenti dengan jawaban yang salah.

​	**Struktur data** adalah cara untuk menyimpan dan mengatur data untuk menfasilitasi akses dan modifikasi. Tidak ada struktur data tunggul yang bekerja denganbaik untuk semua tujuan, jadi penting untuk mengetahui kekuatan dan keterbatasaan beberapa di antaranya.

​	**Menganalisis suatu algoritma** berarti memprediksi sumber daya yang algoritma butuhkan.

## B. IMPORTING PROBLEM TYPES 

### 1. Sorting

**Sorting Problem** adalah mengatur ulang array atau daftar elemen yang diberikan menurut operator perbandingan pada elemen. Operator perbandingan digunakan untuk menentukan orde baru elemen dalam struktur data masing-masing.

### 2. Searching

**Searching Problem** berkaitan dengan menemukan nilai yang diberikan, yang disebut kunci pencarian (***search key***), dalam sekelompok data tertentu.

### 3. String Processing

**String** adalah susunan karakter alfabet . Satu masalah khusus yaitu mencari kata tertentu dalam sebuah teks yang disebut **String Matching**

### 4. Graph Problem

Graph dapat dianggap sebagai kumpulan titik yang disebut simpul, beberapa di antaranya dihubungkan oleh segmen garis yang disebut tepi. Beberapa masalah grafik yang paling terkenal adalah **Traveling Salesman Problem (TSP)** dan **Masalah Pewarnaan Graf**.

### 5. Combinatorial Problem

Dari perspektif yang lebih abstrak, masalah travelling salesman dan masalah pewarnaan graf adalah contoh dari **masalah kombinatorial**. Ini adalah masalah yang meminta, secara eksplisit atau implisit, untuk menemukan objek kombinatorial seperti permutasi, kombinasi, atau subset yang memenuhi batasan tertentu.

### 6. Geometric Problem

**Algoritma geometri** berurusan dengan objek geometris seperti titik, garis, dan poligon. Dua masalah geometric problem  ialah **the closest-pair problem** dan **the convex-hull problem**. 

### 7. Numerical Problem

**Masalah numerik** adalah masalah yang melibatkan objek matematika yang bersifat kontinu: memecahkan persamaan dan sistem persamaan, menghitung integral tertentu, mengevaluasi fungsi, dan sebagainya.

## C. BRUTE FORCE & EXHAUSTIVE SEARCH

**Brute force** adalah pendekatan langsung untuk memecahkan masalah, biasanya langsung berdasarkan pernyataan masalah dan definisi konsep yang terlibat.

### 1. Selection Sort 

#### a. Overview

**Selection Sort** mengurutkan array dengan berulang kali menemukan  elemen minimum (dengan mempertimbangkan urutan menaik) dari bagian yang  tidak diurutkan dan meletakkannya di awal.

**Analisis Performa**

- Time Complexity: $$O(n^2)$$
- Space Complexity: $$O(1)$$

**Selection Sort Digunakan Ketika**:

- List yang ingin diurutkan berukuran kecil
- Biaya Swapping tidak menjadi masalah
- Wajib untuk memeriksa elemen secara keseluruhan

#### b. Pseudocode - Algoritma

```
SelectionSort(A)
for i=0 to n-2 do
	min=i
	for j=i+1 to n-1 do
		if A[j] < A[min] 
			min = j
	swap A[i] and A[min]
```

#### c. Code Python

```
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
```

### 2. Bubble Sort

#### a. Overview

**Bubble Sort** adalah algoritma pengurutan paling sederhana yang bekerja dengan menukar elemen yang berdekatan berulang kali jika urutannya salah.

**Analisis Performa**

- Time Complexity :
  - Worst Case : $$O(n^2)$$ 
  - Best Case : $$O(n)$$
  - Average Case : $$O(n^2)$$ 
- Space Complexity : 
  - Before Optimized : $$O(1)$$
  - After Optimized : $$O(2)$$

**Bubble Sort Digunakan Ketika :**

- Kompleksitas tidak dipermasalahkan
- Kode pendek dan sederhana lebih disukai

#### b.Pseudocode - Algoritma

```
BubleSort(A)
	for i=0 to n-2 do
		for j=0 to n-2-i
			if A[j+1]<A[j] 
				swap A[j] and A[j+1]
```

#### c. Code Python

```
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
```

### 3. Sequantial Search

#### a.Overview

**Sequantial Search** juga disebut pencarian linear. Pencarian dimulai pada item pertama dan bergerak melalui setiap item sampai item yang dicari diperoleh atau item telah ditelusuri semua.

#### b. Pseudocode - Algoritma

```
SequentialSearch(A, K)
	A[n] = K
	i = 0
	while A[i] != K do
		i = i+1
	if i<n 
		return i
	else 
		return -1
```

#### c. Code - Python

```
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
```

### 4. Brute-Force String Maching

#### a. Overview

**String Matching** adalah proses menemukan substring dari suatu teks yang cocok dengan pola yang diberikan.

#### b. Pseudocode - Algoritma

```
BruteForceStringMatch(T[0..n-1], P[0..m-1])
for i=0 to n-m do
	j = 0
	while j<m and P[j] = T[i+j] do
		j = j+1
	if j=m 
		return i
return -1
```

#### c. Code - Python

```
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
```



### 5. Closest-Pair Problem by Brute Force

#### a. Overview

**Closest-Pair Problem** atau masalah pasangan titik terdekat adalah masalah geometri komputasi, pada masalah ini diberikan n titik dalam ruang metrik, kemudian diminta menemukan pasangan titik dengan jarak (Euclidean) terkecil di antara mereka. 

#### b. Pseudocode - Algoritma

```
BruteForceClosesrPair(P)
d = infinity
for i=1 to n-1 do
	for j=1+1 to n do
		d = min(d,sqrt((xi-xj)^2)+(yi-yj)^2))
```



#### c. Code - Python

```
import math

def euclid_distance(p1, p2):
  return math.sqrt((p1.x - p2.x)**2 + (p1.y - p2.y)**2)

def brute_force_closest(P):
    min_d = float('inf')
    for i in range(len(P)):
        for j in range(i + 1, len(P)):
            if euclid_distance(P[i], P[j]) < min_d:
                min_d = euclid_distance(P[i], P[j])
    
    return min_d

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

input = [Point(5,2), Point(2,7), Point(10,16),
          Point(34,50), Point(3,6), Point(20,5),
          Point(12,4), Point(8,9), Point(5,21)]
          
cp = brute_force_closest(input)
print("Closest Pair :", cp)
```



### 6. Convex-Hull Problems by Brute Force

#### a. Overview

**Convex hull** dari himpunan titik S dapat didefinisikan sebagai himpunan convex yang berisi S. (Persyaratan "terkecil" berarti bahwa Convex Hull dari S harus merupakan himpunan bagian dari himpunan cembung yang berisi S)

#### b. Pseudocode - Algoritma

```
-
```



#### c. Code - Python

```
-
```



### 7. TSP

#### a. Overview

Seorang sales perlu mengunjungi semua kota dari daftar, di mana jarak antara semua kota diketahui dan setiap kota harus dikunjungi sekali saja. Apa rute terpendek yang mungkin dia kunjungi setiap kota tepat satu kali dan kembali ke kota asal?

#### b. Pseudocode - Algoritma

```
-
```

#### c. Code

```
-
```



### 8. Knapsack Problem

#### a. Overview

Dalam **Knapsack Problem**, Anda perlu mengemas satu set barang, dengan nilai dan ukuran tertentu (seperti berat atau volume), ke dalam wadah dengan kapasitas maksimum. Jika ukuran total barang melebihi kapasitas, Anda tidak dapat mengemas semuanya. Dalam hal ini, masalahnya adalah memilih subset dari item dengan nilai total maksimum yang akan muat dalam wadah.

#### b. Pseudocode - Algoritma

```
-
```



#### c. Code

```
-
```



### 9 Assignment Problem

#### a. Overview

Salah satu masalah optimasi kombinatorial yang paling terkenal adalah **masalah penugasan (Assignment Problem)**. Berikut ini contohnya: misalkan sekelompok pekerja perlu melakukan serangkaian tugas, dan untuk setiap pekerja dan tugas, ada biaya untuk menugaskan pekerja ke tugas tersebut. Masalahnya adalah menugaskan setiap pekerja ke paling banyak satu tugas, tanpa ada dua pekerja yang melakukan tugas yang sama, sambil meminimalkan total biaya.

#### b. Pseudocode

```
-
```

#### c. Code

````
-
````



### 10. DFS



### 11. BFS







### 1. Insertion Sort
#### a. Overview
​	Insertion Sort adalah algoritme pengurutan sederhana yang bekerja mirip dengan cara Anda mengurutkan kartu remi di tangan Anda. Array hampir dipecah menjadi bagian yang diurutkan dan tidak disortir. Nilai dari bagian yang tidak disortir diambil dan ditempatkan pada posisi yang benar di bagian yang diurutkan.

**Analisis Performa**

- Time Complexity: $$O(n^2)$$
- Space : $$O(1)$$
- Paradigma Algoritma: Pendekatan Inkremental

#### b. Pseudocode
**Pseudocode: Algoritma Insertion Sort** 
```
INSERTION-SORT(A)
for j=1 to A.length
	key = A[j]
	//Insert A[j] into the sorted sequence A[0..j-1]
	i = j-1
	while i>=0 and A[i] > key
		A[i+1] = A[i]
		i = i - 1
	A[i+1] = key
```

#### c. Code
**Python Program**: 

*InsertionSort.py*

```
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
```


### **2. Merge sort - Devide and Conquer**

#### a. Overview 

Paradigma devide and conquer melibatkan tiga langkah pada setiap tingkat rekursi :

**Divide** : Bagi masalah masalah menjadi beberapa submasalah yang merupakan contoh yang lebih kecil dari permasalahan yang sama

**Conquer** : Taklukkan submasalah dengan menyelesaikan secara rekursif. Namun jika ukuran submasalah cukup kecil, selesaikan saja submasalah secara langsung. 

**Combine** : Menggabungkan solusi untuk submasalah ke dalam solusi masalah asli.




Algoritma merge-sort mengikuti paradigma divide and conquer

**Divide**: Bagi barisan n-element yang akan diurutkan menjadi dua suburutan masing-masing n=2 elemen

**Conquer**: Mengurutkan dua suburutan secara rekursif menggunakan merge sort

**Combine**: Menggabungkan dua suburutan yang diurutkan untuk menghasilkan jawaban yang diurutkan



**Analisis Performa**

- Time Complexity: $$O(nLogn)$$

- Space : $$O(n)$$

- Paradigma Algoritma: Devide and Conquer

  


#### b. Pseudocode

**Pseudocode : Algoritma MergeSort**

```
MERGE-SORT(A)
	if A.length > 1
		n = math.round(A.length/2)
		leftA = A[0 .. n]
		rightA = A[n ... A.length-1]
		
		MERGE-SORT(leftA)
		MERGE-SORT(rightA)
		
		i = 0
		j = 0
		k = 0
		
		while (i < leftA.length && j < rightA.length)
			if leftA[i] < rightA[j]
				A[k] = leftA[i]
				i = i + 1
			else
				A[k] = rightA[j]
				j = j + 1
			k = k + 1
		
		while (i < leftA.length)
			A[k] = leftA[i]
			i = i + 1
			k = k + 1
			
		while (j < leftA.length)
			A[k] = rightA[j]
			j = j + 1
			k = k + 1
```

#### c. Code

**Python Program**

*MergeSort.py*

```
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

```













