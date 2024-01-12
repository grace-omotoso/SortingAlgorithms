# The Bubble sort algorithm

def bubble_sort(array):
    swap = False
    for i in range(len(array)):
        for j in range(i+1, len(array)):
            if array[j] < array[i]:
                array[j], array[i] = array[i], array[j]
                swap == True
        if swap == False:
            return array
            
    return array

def main():
    array = [65, 78, 23, 17, 45, 90, 2, 17]
    sorted_array = bubble_sort(array)
    print(sorted_array)

main()
            
            
