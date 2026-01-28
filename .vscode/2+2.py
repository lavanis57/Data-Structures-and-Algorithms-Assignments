import random 
sample = random.sample(range(1,100000), 1000)

def partition(arr, low, high):
    pivot = arr[high] #Need not be the optimal choice of pivot, could be improved
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quick_sort(arr, low = 0, high = None):
    if low < high:
        pivot = partition(arr, low, high)
        quick_sort(arr, low, pivot - 1)
        quick_sort(arr, pivot + 1, high)
    return arr

print(quick_sort(sample, low = 0, high = len(sample)-1))
