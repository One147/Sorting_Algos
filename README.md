# Sorting_Algos
Learning about common sorting algos and when/why they should be implemented

In order to better encapsulate the speed/efficiency/process of different sorting algos, I created a program that visualizes how the sorting algos sort as well as the speed that they sort at.

**Sorting algo can be changed by opening the "Rectangle Demonstration Sorting.py" file and heading to the comment stating " #specific sorting algo is called here (changable)." This func can be changed to any of the methods available above in the source code in order to see the results.

![pygame window 2023-05-16 17-24-57_Trim](https://github.com/One147/Sorting_Algos/assets/122568488/2492fa29-5548-4364-848e-612cd4ae091a)
**This is an example of selection sort being visualized**

After doing more research on the time complexities and the sorting algo, I used the matplotlib data scinece library to generate a program that displays a live time complexity of each sorting algo. This is done by first running the testing_algorythms_for_sorting.py file. This file generates a forever increasing list of random values which are then sorted by each algo. The amount of instances and the time each algo took to sort the list is then written onto a csv file

This csv file is then used by the Time_complex_graph.py file to generate an updating line graph with the number of instances on the x axis and time on the y axis to visualize the time complexities. **certain time complexities can be commented out in this source code to have a more scalable representation of algos**

![sorting algos](https://github.com/One147/Sorting_Algos/assets/122568488/2f3ea4dc-2668-46b1-9569-9c6d9ee902e1)
**This an example of the time complexities of Bubble, Selection, and Tim sort in extremely basic data

**Below is the documentation of research I did in order to learn when/why to use specific sorting algos**
https://docs.google.com/document/d/18pF6D5854FN6nHuaB5UzNTq5GUYDtEU_dR-rBhKKCRc/edit?usp=sharing
