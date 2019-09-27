import time
import sys
import re

# Selection Sort
def Selection_Sort(list):
    # Traverse through givent unsorted list
    for i in range(len(list)):
        # Set first element's index as min_index
        min_index = i

        # Traverse through the rest of the unsorted list
        for j in range(i + 1, len(list)):
            # If a smaller element is found, set the new index
            if (list[min_index] > list[j]):
                min_index = j

        # Swap the first element with the smallest element        
        list[i], list[min_index] = list[min_index], list[i]
    return list

# Insertion Sort
def Insertion_Sort(list):
    # Traverse through the unsorted list
    # Started with the second element
    for i in range (1, len(list)):
        # Set the element that is going to be 'moved'
        # as the 'key'
        key = list[i]

        # The key will be compared to elements before it
        j = i-1
        # Check if the key is smaller than the
        # element before it
        while (key < list[j]) and (j >= 0):
            # Increase the element's index by 1
            list[j + 1] = list[j]
            # Check the element before the current
            j -= 1
        # Set the new index of the key
        list[j + 1] = key
    return list

# Merge Sort
def Merge_Sort(list):
    if (len(list) > 1):
        mid = len(list) // 2 # Find middle of list
        Left = list[:mid]    # List left of mid
        Right = list[mid:]   # List right of mid

        Merge_Sort(Left)     # Split and sort new list
        Merge_Sort(Right)
        i = j = k = 0

        # Move elements to correct position
        while (i < len(Left) and j < len(Right)):
            if (Left[i] < Right[i]):
                list[k] = Left[i]
                i += 1
            else:
                list[k] = Right[j]
                j += 1
            k += 1

        # Check if there are any more elements
        while (i < len(Left)):
            list[k] = Left[i]
            i += 1
            k += 1
        while (j < len(Right)):
            list[k] = Right[j]
            j += 1
            k += 1
    return list

    # Time Selection Sort
def Run_Selection(list):
    start_time = time.perf_counter() # Start Timer
    selection_list = (Selection_Sort(list)) # Call Selection Sort
    end_time = time.perf_counter() # End Timer
    runtime = (end_time - start_time) * 1000 # Calculate and convert to milliseconds

    # Print Result to stdout
    print('Selection Sort (' + '%0.2f' % float(runtime) + ' ms): ', end='')
    print(*selection_list, sep=', ')

    # Time Insertion Sort
def Run_Insertion(list):
    start_time = time.perf_counter() # Start Timer
    insertion_list = (Insertion_Sort(list)) # Call Selection Sort
    end_time = time.perf_counter() # End Timer
    runtime = (end_time - start_time) * 1000 # Calculate and convert to milliseconds

    # Print Result to stdout
    print('Insertion Sort (' + '%0.2f' %float(runtime) + ' ms): ', end='')
    print(*insertion_list, sep=', ')

    # Time Merge Sort
def Run_Merge(list):
    start_time = time.perf_counter() # Start Timer
    merge_list = (Merge_Sort(list)) # Call Selection Sort
    end_time = time.perf_counter() # End Timer
    runtime = (end_time - start_time) * 1000 # Calculate and convert to milliseconds

    # Print Result to stdout
    print('Merge Sort     (' + '%0.2f' %float(runtime) + ' ms): ', end='')
    print(*merge_list, sep=', ') 


# Main function to run when program is called
def main():
    file = open(sys.argv[1], 'r') # Open given argument
    list = file.read() # Read the inputed file
    file.close()
    list = list.replace(',','').strip().split() # Strip \n and commas, then split the numbers by white spaces

    # Convert String to ints
    for i in range (len(list)):
        list[i] = (int(list[i]))

    Run_Selection(list)
    Run_Insertion(list)
    Run_Merge(list)

if __name__=="__main__":
    main()
    