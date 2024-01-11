# The selection sort algorithm

def selection_sort(array):
    for i in range(len(array)):
        min_idx = i
        for j in range(i+1, len(array)):
            if array[j] < array[min_idx]:
                min_idx = j
        # put min_idx element in ith position
        array[min_idx],array[i] = array[i],array[min_idx]
    return array

def main():
    array = [65, 78, 23, 17, 45, 90, 2, 17]
    sorted_array = selection_sort(array)
    print(sorted_array)

main()


        
        
