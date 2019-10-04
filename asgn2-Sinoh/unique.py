import sys

# Finds the singleton element, if None returns None
def unique(list, first, last):

    if (first > last): # Base Case
        return None
    
    if (first == last):     # If only one element left
        return list[first]

    mid = int(first + (last - first) / 2) # Get middle index

    if (mid % 2): # Middle index is odd
        if  (list[mid] == list[mid - 1]): # Element right of mid
            return unique(list, mid + 1, last) 
        else: # Element left of mid
            return unique(list, first, mid - 1)

    else: # Middle index is even
        if  (list[mid] == list[mid + 1]): # Element right of mid
            return unique(list, mid + 2, last)
        else: # Element left of mid
            return unique(list, first, mid)


# Main function to run when program is called
def main():
    file = open(sys.argv[1], 'r') # Open given argument
    list = file.read() # Read the inputed file
    file.close()
    list = list.replace(',','').strip().split() # Strip \n and commas, then split the numbers by white spaces

    # Convert String to ints
    for i in range (len(list)):
        list[i] = (int(list[i]))

    # Print singleton to stdout
    print(unique(list, 0, len(list) - 1))

if __name__=="__main__":
    main()
    
    