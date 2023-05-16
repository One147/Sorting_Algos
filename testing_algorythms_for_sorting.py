
#libraries

import random
import time
import csv

#sorting list and loop tick rate
sort_list= []
tick = 0

#sorting algos 
def mergeSort(arr):
    if len(arr) > 1:
 
         # Finding the mid of the array
        mid = len(arr)//2
 
        # Dividing the array elements
        L = arr[:mid]
 
        # into 2 halves
        R = arr[mid:]
 
        # Sorting the first half
        mergeSort(L)
 
        # Sorting the second half
        mergeSort(R)
 
        i = j = k = 0
 
        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
 
        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
 
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

    #

def printList(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()

def bubble_sort(list):
    indexing_length = len(list) - 1

    sorted = False
    while not sorted:
        sorted = True
        for i in range(0, indexing_length):
            if list[i] > list[i+1]:
                sorted = False
                list[i] , list[i+1] = list[i+1] , list[i]

    return list

def quick_sort(list, l, h):
    if l < h:
        partition_pos = partition(list, l, h)
        quick_sort(list, l, partition_pos - 1)
        quick_sort(list, partition_pos + 1, h)

def partition(list, l, h):
    i = l
    j = h - 1
    pivot = list[h]
    
    while i < j: #before i and j cross
        
        while i < h and list[i] < pivot:
            i += 1
        while j > l and list[j] >= pivot:
            j -= 1
            
        if i < j:
            list[i], list[j] = list[j], list[i]
    
    if list[i] > pivot:
        list[i], list[h] = list[h], list[i]
        
    return i

def selection_sort(list):
        for index in range(len(list)): #acquiring the indexes of the list 
            
            target_minimum_index = index #target index (the index location of the next minimum on the list. This starts off as the next value on the list)
            for comparison_index in range(index + 1 , len(list)): #acquiring next index in list to the end of list   
                
                if list[comparison_index] < list[target_minimum_index]: #now we sort the values of each index and if the value of the next index is lower, we swap
                    list[comparison_index] , list[target_minimum_index] = list[target_minimum_index] , list[comparison_index]
        return list




#list generator and sort tester
while True:
    
    tick += 1
    
    #increase sort index by tick 
    for i in range(tick):
        sort_list.append(i)
    
    #changing values on the list to random values
    for i in range(len(sort_list)):
        sort_list[i] = random.randint(-9999,9999)

    #use sort methods to return a sorted list and get the time it takes to do so
    
    #selection sort
    initial_selection_time = time.time()
    selection_sort(sort_list)
    final_selection_time = time.time() - initial_selection_time 
    
    #changing values on the list to random values
    for i in range(len(sort_list)):
        sort_list[i] = random.randint(-999,999)
    
    #merge sort
    initial_merge_time = time.time()
    mergeSort(sort_list)
    final_merge_time = time.time() - initial_merge_time 
    
      #changing values on the list to random values
    for i in range(len(sort_list)):
        sort_list[i] = random.randint(-999,999)
    
    #quick sort
    initial_quick_time = time.time()
    quick_sort(sort_list, 0, len(sort_list) - 1)
    final_quick_time = time.time() - initial_quick_time 
        
      #changing values on the list to random values
    for i in range(len(sort_list)):
        sort_list[i] = random.randint(-999,999)
    
    #bubble sort
    initial_bubble_time = time.time()
    bubble_sort(sort_list)
    final_bubble_time = time.time() - initial_bubble_time 
    
     #changing list to random values
    for i in range(len(sort_list)):
        sort_list[i] = random.randint(-999,999)
        
    #built in python Timsort (a combination of insertion and merge sort)
    initial_tim_time = time.time()
    sort_list.sort()
    final_tim_time = time.time() - initial_tim_time
    
    #creating/opening csv file with time complexity data and writing instances/time taken to csv file
    with open("time_complexity_data.csv" , "a", newline = "") as csvfile:
        
        #creating headers/fieldnames for number of values sorted and the time it took to sort these values
        fieldnames = ["n (instances)" , "Selection Sort Time (s)" ,"Merge Sort Time (s)" , "Quick Sort Time (s)", "Bubble Sort Time (s)", "Tim Sort Time (s)"]
        
        #create a writer object using the dictwriter class writing the file type (csvfile) with the given fieldnames
        thewriter = csv.DictWriter(csvfile, fieldnames = fieldnames)
        
        #writes the header on the first instance of the while loop
        if tick == 1:
            thewriter.writeheader()
        
        thewriter.writerow({ 
                                
                                "n (instances)" : len(sort_list), 
                                "Selection Sort Time (s)" : final_selection_time,
                                "Merge Sort Time (s)" : final_merge_time, 
                                "Quick Sort Time (s)" : final_quick_time,
                                "Bubble Sort Time (s)" : final_bubble_time,
                                "Tim Sort Time (s)" : final_tim_time,
                                  
            })