# Bubble sort
def Bubblesort():
    global v
    n = len(v)
    for i in range(n):
        for j in range(0, n - i - 1):
            if int(v[j]) > int(v[j + 1]):
                v[j], v[j + 1] = v[j + 1], v[j]


# Count sort
def Countsort():
    max1 = 0
    global v
    n = len(v)
    max1 = max(v)
    fin = []
    w = [0] * (max1 + 1)
    for i in range(n):
        w[v[i]] += 1
    for j in range(max1 + 1):
        c = w[j]
        while c > 0:
            fin.append(j)
            c -= 1
    v = fin


# Radixsort
def count_for_radix_sort(arr, exp):
    n1 = len(arr)
    output = [0] * n1
    count = [0] * 10

    for i in range(0, n1):
        index = (arr[i] / exp)
        count[int((index) % 10)] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]


    i = n - 1
    while i >= 0:
        index = (arr[i] / exp)
        output[count[int((index) % 10)] - 1] = arr[i]
        count[int((index) % 10)] -= 1
        i -= 1

    i = 0
    for i in range(0, len(arr)):
        arr[i] = output[i]

def radixSort(v):
    max1 = max(v)
    exp = 1
    while max1 / exp > 0:
        count_for_radix_sort(v, exp)
        exp *= 10


# Quicksort
def pivot(v, st, dr):
    i = st - 1
    piv = v[dr]
    for j in range(st, dr):
        if v[j] <= piv:
            i += 1
            v[i], v[j] = v[j], v[i]
    v[i + 1], v[dr] = v[dr], v[i + 1]
    return i + 1


def quicksort(v, st, dr):
    if st < dr:
        piv = pivot(v, st, dr)
        quicksort(v, st, piv - 1)
        quicksort(v, piv + 1, dr)


# Mergesort
def interclasare(lst, ldr):
    i = j = 0
    rez = []
    while i < len(lst) and j < len(ldr):
        if lst[i] < ldr[j]:
            rez.append(lst[i])
            i += 1
        else:
            rez.append(ldr[j])
            j += 1
    rez.extend(lst[i:])
    rez.extend(ldr[j:])
    return rez


def mergesort(v):
    if len(v) <= 1:
        return v
    else:
        mij = len(v) // 2
        st = mergesort(v[:mij])
        dr = mergesort(v[mij:])
        return interclasare(st, dr)


import random

n = int(input("Numar de elemente:"))
k = int(input("Marimea maxima a unui element:"))
v = []
import time

if n <= 3000:
    for i in range(n):
        v.append(int(random.randrange(k)))
    w = v
    t1 = time.time_ns() / (10 ** 9)
    Bubblesort()
    t2 = time.time_ns() / (10 ** 9)
    ok = 1
    for i in v:
        if i not in w:
            ok = 0
    if ok == 1 and len(w) == len(v):
        print("Bubblesort nu a modificat  lista initiala si a scos urmatorul timp:", t2 - t1)
    else:
        print("Dupa sortare bubble sort a modificat lista initiala")
else:
    print("Bubblesort este prea ineficient pentru lungimi de liste > 3000")

v = []
if n <= 100000 and k <= 100000:
    for i in range(n):
        v.append(int(random.randrange(k)))
    w = v
    t1 = time.time_ns() / (10 ** 9)
    Countsort()
    t2 = time.time_ns() / (10 ** 9)
    ok = 1
    for i in v:
        if i not in w:
            ok = 0
    if ok == 1 and len(w) == len(v):
        print("Countsort nu a modificat  lista initiala si a scos urmatorul timp:", t2 - t1)
    else:
        print("Dupa sortare countsort a modificat lista initiala")
else:
    print("Countsort nu mai este eficient pentru numere > 100000")

v = []
if n <= 10000:
    for i in range(n):
        v.append(int(random.randrange(k)))
    w = v
    t1 = time.time_ns() / (10 ** 9)
    radixSort(v)
    t2 = time.time_ns() / (10 ** 9)
    ok = 1
    for i in v:
        if i not in w:
            ok = 0
    if ok == 1 and len(w) == len(v):
        print("Radixsort nu a modificat  lista initiala si a scos urmatorul timp:", t2 - t1)
    else:
        print("Dupa sortare radixsort a modificat lista initiala")
else:
    print("Radixsort nu mai este eficient pentru numar de elemente/dimensiunea elementelor > 10000")

v = []
if n < 1000000:
    for i in range(n):
        v.append(int(random.randrange(k)))
    w = v
    t1 = time.time_ns() / (10 ** 9)
    quicksort(v, 0, n - 1)
    t2 = time.time_ns() / (10 ** 9)
    ok = 1
    for i in v:
        if i not in w:
            ok = 0
    if ok == 1 and len(w) == len(v):
        print("Quicksort nu a modificat  lista initiala si a scos urmatorul timp:", t2 - t1)
    else:
        print("Dupa sortare quicksort a modificat lista initiala")

    v = []
    for i in range(n):
        v.append(int(random.randrange(k)))
    w = v
    t1 = time.time_ns() / (10 ** 9)
    mergesort(v)
    t2 = time.time_ns() / (10 ** 9)
    ok = 1
    for i in v:
        if i not in w:
            ok = 0
    if ok == 1 and len(w) == len(v):
        print("Mergesort nu a modificat  lista initiala si a scos urmatorul timp:", t2 - t1)
    else:
        print("Dupa sortare mergesort a modificat lista initiala")
else:
    print("Quicksort dureaza mai mult de 5 secunde pentru numar de elemente>1000000")
    print("Mergesort dureaza mai mult de 5 secunde pentru numar de elemente>1000000")

if n < 10000000:
    v = []
    for i in range(n):
        v.append(int(random.randrange(k)))
    w = v
    t1 = time.time_ns() / (10 ** 9)
    v.sort()
    t2 = time.time_ns() / (10 ** 9)
    ok = 1
    for i in v:
        if i not in w:
            ok = 0
    if ok == 1 and len(w) == len(v):
        print("Sortarea predefinita nu a modificat  lista initiala si a scos urmatorul timp:", t2 - t1)
    else:
        print("Dupa sortarea predefinita s-a modificat lista initiala")
else:
    print("Sortarea predefinita dureaza mai mult de 6 secunde pentru lungimi > 10 milioane")