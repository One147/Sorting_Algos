from matplotlib import pyplot as plt
import csv
import random
import time
import pandas as pd
from matplotlib.animation import FuncAnimation




#Graph title
plt.title("Time Complexities of Different Sorting Algorithms")




def animate_graph(i):
    #read csv
    data = pd.read_csv("time_complexity_data.csv")
    sort_n = data["n (instances)"]
    selection_time = data["Selection Sort Time (s)"]
    merge_time = data["Merge Sort Time (s)"]
    quick_time = data ["Quick Sort Time (s)"]
    bubble_time = data["Bubble Sort Time (s)"]
    tim_time = data["Tim Sort Time (s)"]
    
    
    #clear plot and represent data
    plt.cla()
    #selection sort
    plt.plot(sort_n, selection_time, c="red" , label = "Selection Sort" , linewidth = 1)
    # plt.plot(sort_n, merge_time, c="green" , label = "Merge Sort" , linewidth = 1)
   # plt.plot(sort_n, quick_time, c="blue" , label = "Quick Sort" , linewidth = 1)
    plt.plot(sort_n, bubble_time, c="black" , label = "Bubble Sort" , linewidth = 1)
    plt.plot(sort_n, tim_time, c= "orange" , label = "Tim Sort" , linewidth = 1)
    plt.legend()
      
    
    

    
ani = FuncAnimation(plt.gcf(), animate_graph, interval = 1)
plt.show()



