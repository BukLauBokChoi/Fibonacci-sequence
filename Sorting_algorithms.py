# insertion sort with two for loops

def insertion_sort(A):
    for i in range(1, len(A)):
        for j in range(i-1, -1, -1):
            if A[j] > A[j+1]:
                A[j], A[j+1] = A[j+1], A[j]
            else: 
                break

A = [1, 3, 6, 4, 2, 7, 0]
insertion_sort(A)
print(A)

# insertion sort with a while loop

def insertion_sort1(A1):
    for i in range(1, len(A1)):
        while A1[i-1] > A1[i] and i-1 >= 0:
            A1[i-1], A1[i] = A1[i], A1[i-1]
            i -= 1

A1 = [1, 3, 6, 4, 2, 7, 0]
insertion_sort1(A1)
print(A1)

# selection sort with two for loops

def selection_sort(A2):
    for i in range(len(A2)-1):
        minVal = i
        for j in range(i+1, len(A2)):
            if A2[j] < A2[minVal]:
                minVal = j
        if minVal != i:
            A2[minVal], A2[i] = A2[i], A2[minVal]
        
A2 = [1, 3, 6, 4, 2, 7, 0]
selection_sort(A2)
print(A2)

# bubble sort with two for loops

def bubble_sort(A3):
    for i in range(len(A3)-1):
        for j in range(len(A3)-i-1):
            if A3[j] > A3[j+1]:
                A3[j], A3[j+1] = A3[j+1], A3[j]

A3 = [1, 3, 6, 4, 2, 7, 0]
bubble_sort(A3)
print(A3)