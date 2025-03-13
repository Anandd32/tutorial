def bubble_sort(l):
    n = len(l)
    for i in range(n):
        for j in range(0, n-i-1):
            if l[j] > l[j+1]:
                l[j],l[j+1] = l[j+1],l[j]

n = int(input("Enter the number of elements: "))
numbers = [int(input(f"Enter number {i+1}: ")) for i in range(n)]

bubble_sort(numbers)
print(f"\nSorted list in non-decreasing order: {numbers}")
