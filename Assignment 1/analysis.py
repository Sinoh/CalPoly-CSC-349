from algorithms import Selection_Sort
from algorithms import Insertion_Sort
from algorithms import Merge_Sort
import random
import time
import sys

def Run_Selection(list, output):
    start_time = time.perf_counter() # Start Timer
    Selection_Sort(list) # Call Selection Sort
    end_time = time.perf_counter() # End Timer
    runtime = (end_time - start_time) * 1000 # Calculate and convert to milliseconds

    # Print Result to stdout
    output.write('%0.2f' % float(runtime) + '\n')

    # Time Insertion Sort
def Run_Insertion(list, output):
    start_time = time.perf_counter() # Start Timer
    Insertion_Sort(list) # Call Selection Sort
    end_time = time.perf_counter() # End Timer
    runtime = (end_time - start_time) * 1000 # Calculate and convert to milliseconds

    # Print Result to stdout
    output.write('%0.2f' %float(runtime) + '\n')

    # Time Merge Sort
def Run_Merge(list, output):
    start_time = time.perf_counter() # Start Timer
    Merge_Sort(list) # Call Selection Sort
    end_time = time.perf_counter() # End Timer
    runtime = (end_time - start_time) * 1000 # Calculate and convert to milliseconds

    # Print Result to stdout
    output.write('%0.2f' %float(runtime) + '\n')

def main():

    select_out = open("select_out.txt", "w")
    insert_out = open("insert_out.txt", "w")
    merge_out = open("merge_out.txt", "w")

    count = 0
    percent = 0
    for i in range(5000,10000, 10):
        list = random.sample(range(0, 10000), i)
        Run_Selection(list, select_out)
        if (count % 15 == 0):
            print(percent, '%')
            percent += 1
        count += 1

    for i in range(5000,10000, 10):
        list = random.sample(range(0, 10000), i)
        Run_Insertion(list, insert_out)
        if (count % 15 == 0):
            print(percent, '%')
            percent += 1
        count += 1

    for i in range(5000,10000, 10):
        list = random.sample(range(0, 10000), i)
        Run_Merge(list, merge_out)
        if (count % 15 == 0):
            print(percent, '%')
            percent += 1
        count += 1
    
    select_out.close()
    insert_out.close()
    merge_out.close()
if __name__=="__main__":
    main()