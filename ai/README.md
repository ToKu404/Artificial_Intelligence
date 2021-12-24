# ALGRORITMA DAN STRUKTUR DATA

### A. Definisi Dasar 

​	**Algoritma** adalah prosedur komputasi yang terdefinisi dengan baik yang mengambil beberapa nilai, atau seperangkat nilai, sebagai **input** dan menghasilkan beberapa nilai, atau seperangkat nilai sebagai **output.** Algoritma merupakan urutan langkah-langkah komputasi yang mengubah input ke dalam output. Algotima juga dapat dilihat sebagai alat untuk **memecahkan masalah komputasi** yang ditentukan dengan baik.

Algoritma dikatakan **true** jika, untuk setiap contoh input, itu berhenti dengan output yang benar. Algoritma yang benar memecahkan masalah komputasi yang diberikan. Algoritma yang **false** mungkin tidak berhenti sama sekali pada beberapa contoh input atau mungkin berhenti dengan jawaban yang salah.

​	**Struktur data** adalah cara untuk menyimpan dan mengatur data untuk menfasilitasi akses dan modifikasi. Tidak ada struktur data tunggul yang bekerja denganbaik untuk semua tujuan, jadi penting untuk mengetahui kekuatan dan keterbatasaan beberapa di antaranya.

​	**Menganalisis suatu algoritma** berarti memprediksi sumber daya yang algoritma butuhkan.



### B. Algoritma Sorting

Algoritma Penyortiran digunakan untuk mengatur ulang array atau daftar elemen yang diberikan menurut operator perbandingan pada elemen. Operator perbandingan digunakan untuk menentukan orde baru elemen dalam struktur data masing-masing.

**Input : ** Urutan *n* numbers $$(a_1, a_2, ... a_n)$$  .

**Output :**  Permutasi (Penyusunan Ulang) $$(a'_1,a'_2, ..., a'_n)$$ dari input yang diberikan menjadi  $$a'_1\le a'_2\le ... \le a'_n$$

#### 1. Insertion Sort

​	Insertion Sort adalah algoritme pengurutan sederhana yang bekerja mirip dengan cara Anda mengurutkan kartu remi di tangan Anda. Array hampir dipecah menjadi bagian yang diurutkan dan tidak disortir. Nilai dari bagian yang tidak disortir diambil dan ditempatkan pada posisi yang benar di bagian yang diurutkan.

<img src="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fwww.studytonight.com%2Fdata-structures%2Fimages%2Fbasic-insertion-sort.png&f=1&nofb=1" alt="drawing" height="600"/>

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

**Python Program**: 

*01/InsertionSort.py*

```
input = [9, 3, 4, 12, 10, 5, 4, 11] # Example Input

def insertionSort(A):
    for j in range(1,len(A)):
        key = A[j] 
        # Insert A[j] into sorted sequence A[0..j-1]
        i = j-1
        while (i>=0 and A[i]>key):
            A[i+1] = A[i]
            i = i - 1
        A[i+1] = key
    print(A)

insertionSort(input)
```



**Analisis dari Insertion Sort**

Performa Prosedur *INSERTION-SORT* dihitung dengan ***cost***  setiap pernyataan dan ***times*** berapa kali setiap pernyataan dieksekusi.

![image-20211224060927533](/home/lunareg/snap/typora/46/.config/Typora/typora-user-images/image-20211224060927533.png)

- Time Complexity: O(n^2)
- Space : O(1)
- Kasus Batas: Pengurutan penyisipan membutuhkan waktu maksimum untuk menyortir jika elemen diurutkan dalam urutan terbalik. Dan dibutuhkan waktu minimum (Orde n) ketika elemen sudah diurutkan.
- Paradigma Algoritma: Pendekatan Inkremental



#### **2. Merge sort - Devide and Conquer**

Banyak algoritma yang memiliki struktur rekursif untuk memecahkan masalah yang diberikan. Algoritma ini **memanggil diri mereka sendiri sekali** atau lebih untuk menangani masalah submasalah terkait. Algoritma ini biasanya mengikut pendekatan **divide and conquer**. 

Paradigma devide and conquer melibatkan tiga langkah pada setiap tingkat rekursi :

**Divide** : Bagi masalah masalah menjadi beberapa submasalah yang merupakan contoh yang lebih kecil dari permasalahan yang sama

**Conquer** : Taklukkan submasalah dengan menyelesaikan secara rekursif. Namun jika ukuran submasalah cukup kecil, selesaikan saja submasalah secara langsung. 

**Combine** : Menggabungkan solusi untuk submasalah ke dalam solusi masalah asli.



Algoritma merge-sort mengikuti paradigma divide and conquer

**Divide**: Bagi barisan n-element yang akan diurutkan menjadi dua suburutan masing-masing n=2 elemen

**Conquer**: Mengurutkan dua suburutan secara rekursif menggunakan merge sort

**Combine**: Menggabungkan dua suburutan yang diurutkan untuk menghasilkan jawaban yang diurutkan

<img src="https://media.geeksforgeeks.org/wp-content/cdn-uploads/Merge-Sort-Tutorial.png" alt="drawing" height="600"/>

**Pseudocode : Prosedur Merge**

ket : *A* adalah array, dan *p,q, dan r* adalah indeks dari array sedemikian rupa sehingga $p\le q < r$. Prosedur mengasumsikan bahwa subarray $A[p..q]$ dan $A[q+1..r]$ yang telah terurut. Kemudian digabungkan untuk membentuk satu subarray yang diurutkan untuk menggantikan subarray $A[p..r]$

```
MERGE(A, p, q, r)
n1 = q - p + 1
n2 = r - q
let L[1..n1 + 1] dan R[1..n2 + 1] be new arrays
for i = 1 to n1
	L[i] = A[p + i - 1]
for j = 1 to n2
	R[j] = A[q+j]
L[n1+1] = infinity
R[n2+1] = infinity
i = 1
j = 1
for k = p to r
	if L[i] <= R[j]
		A[k] = L[i]
		i = i + 1
	else 
		
		A[k] = R[j]
		j = j + 1
```

**Pseudocode: Algoritma Merge Sort**

```
MERGE-SORT(A, p, r)
if p < r
	q = Math.floor((p+r)/2)
	MERGE-SORT(A, p, q)
	MERGE-SORT(A, q+1, r)
	MERGE(A,p,q,r)
```



#### 













