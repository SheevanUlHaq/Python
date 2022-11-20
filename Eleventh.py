def linearSearch(l, el):
    c = 0
    for i in l:
        if (el == i):
            print("Element is present at index: ", c)
            break
        c = c+1
    else:
        print("Element is not present !")


def binarySearch(l1, f, l, el):
    mid = int((f+l)/2)
    if (l1[mid] == el):
        print(el, "is at index ", mid)
        return
    elif (el < l1[mid]):
        binarySearch(l1, f, mid-1, el)
    else:
        binarySearch(l1, mid+1, l, el)
    print("Element is not present !")


def bubbleSort(arr, n):
    for i in range(n-1):
        for j in range(n-1-i):
            if (arr[j] > arr[j+1]):
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
    print("Sorted array is : ", arr)


def seletionSort(arr, n):
    for i in range(n-1):
        min = arr[i]
        for j in range(i+1, n):
            if (arr[j] < min):
                min = arr[j]
                a = j
        temp = arr[i]
        arr[i] = min
        arr[a] = temp
    print("Sorted arrray is : ", arr)


def insertionSort(arr, n):
    for i in range(1, n):
        current = arr[i]
        j = i-1
        while (current < arr[j] and j >= 0):
            arr[j+1] = arr[j]
            j = j-1
        arr[j+1] = current
    print("Soreted array is : ", arr)


print(''' 
\t****************MENU***********
1. Press 1 for linear search.
2. Press 2 for binary search.
3. Press 3 for bubble sort.
4. Press 4 for selecion sort.
5. Press 5 for insertion sort.
6. Press 6 for exit.
''')
choice = int(input("\nEnter your choice : "))
l = []
n = int(input("Enter the no. of elements in the list: "))
for i in range(n):
    # if (choice == 1 or choice == 2):
    #     a = input("Enter the element: ")
    #     l.append(a)
    # else:
    a = int(input('Enter the element: '))
    l.append(a)
while (choice != 6):
    if (choice == 1):
        el = int(input("Enter the element you want to search : "))
        linearSearch(l, el)
    elif (choice == 2):
        el = int(input("Enter the element you want to search : "))
        binarySearch(l, 0, n-1, el)
    elif (choice == 3):
        bubbleSort(l, n)
    elif (choice == 4):
        seletionSort(l, n)
    elif (choice == 5):
        insertionSort(l, n)
    elif (choice == 6):
        exit(0)
    else:
        print("You entered a wrong choice !")
    choice = int(input("Enter your choice: "))
