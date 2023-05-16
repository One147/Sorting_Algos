#libraries

import random
import time
import pygame
import sys

#pygame settings and ititialization 
pygame.init()
screen_width = 600
screen_height = 900
screen = pygame.display.set_mode((screen_width,screen_height))               
clock = pygame.time.Clock()            

#rectangle  and camera classes
class Rectangle(pygame.sprite.Sprite):
    def __init__(self, xpos, ypos, width, height, index, colour):
        super().__init__()
        self.height = height
        self.colour = colour
        self.image = pygame.Surface([width, self.height])
        self.image.fill(self.colour)
        self.rect = self.image.get_rect()
        self.index = index
        self.rect.left = xpos
        self.rect.bottom = ypos

class Camera(pygame.sprite.Sprite):
    def __init__(self, width, height):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([width, height])
        self.image.fill("Black")
        self.rect = self.image.get_rect()
          
    def update(self):
        self.image.fill("Black") #background
        for rects in rect_group:
            self.image.blit(rects.image , rects.rect)

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
def bubble_sort(list, rects):
    indexing_length = len(list) - 1

    sorted = False
    while not sorted:
        sorted = True
        for i in range(0, indexing_length):
            if list[i] > list[i+1]:
                sorted = False
                list[i] , list[i+1] = list[i+1] , list[i]
                for rect in rects:
                        if rect.index == i:
                            rect.kill()
                            rects.add(Rectangle(0 + screen_width/len(list)*i , screen_height , screen_width/len(list), list[i], i, (0,255,0)))
                        if rect.index == i+1:
                            rect.kill()
                            rects.add(Rectangle(0 + screen_width/len(list)*(i+1) , screen_height , screen_width/len(list), list[i+1], i+1, (0,255,0)))
                camera.update()
                screen.blit(camera.image, camera.rect)
                pygame.display.update()
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
        
    return 
def selection_sort(list, rects):
        for index in range(len(list)): #acquiring the indexes of the list 
            
            target_minimum_index = index #target index (the index location of the next minimum on the list. This starts off as the next value on the list)
            
            for rect in rects:
                if rect.index == target_minimum_index:
                    rect.kill()
                    rects.add(Rectangle(0 + screen_width/len(list)*target_minimum_index , screen_height , screen_width/len(list), list[target_minimum_index], target_minimum_index, (0,255,0)))
            
            
            for comparison_index in range(index + 1 , len(list)): #acquiring next index in list to the end of list   
                
                if list[comparison_index] < list[target_minimum_index]: #now we sort the values of each index and if the value of the next index is lower, we swap
                    list[comparison_index] , list[target_minimum_index] = list[target_minimum_index] , list[comparison_index]
                    for rect in rects:
                        if rect.index == comparison_index:
                            rect.kill()
                            rects.add(Rectangle(0 + screen_width/len(list)*comparison_index , screen_height , screen_width/len(list), list[comparison_index], comparison_index, (0,255,0)))
                        if rect.index == target_minimum_index:
                            rect.kill()
                            rects.add(Rectangle(0 + screen_width/len(list)*target_minimum_index , screen_height , screen_width/len(list), list[target_minimum_index], target_minimum_index, (0,255,0)))
                
                    camera.update()
                    screen.blit(camera.image, camera.rect)
                    pygame.display.update()
                    
                    
                    
                                              
                    
                    
        
                    
        return list

#Rectangle sprite group and camera object where sprite group is drawn onto

rect_group = pygame.sprite.Group()
camera = Camera(screen_width, screen_height)

#sorting loop
while True:
    #clearing rectangles and setting background to black
    rect_group.empty()
    screen.fill("Black")
    
    #increase list index by tick^2
    for i in range(tick ** 2):
        sort_list.append(i)
    tick +=1 
    
    #randomize values in list
    for i in range(len(sort_list)):
        sort_list[i] = random.randint(1, screen_height)
        #draw rectangles for every value in the list and screen flip. Rectangle height will corrospond to the value on the list. Rectangle width will corrospond to screen width/list amount
        rect_group.add(Rectangle(0 + screen_width/len(sort_list)*i , screen_height , screen_width/len(sort_list), sort_list[i], i , (255,0,0)))
    
    #update and display camera with the randomized rectangles
    camera.update()
    screen.blit(camera.image, camera.rect)
    pygame.display.update()
    
    #time delay after displaying
    time.sleep(1)
    
    #sort the list (in place algoritihms come with special colour features and real-time sorting view) and record time taken to sort list
    start_time = time.time()
    #specific sorting algo is called here (changable)
    selection_sort(sort_list, rect_group)
    total_time = time.time() - start_time
    
    #empty the rectangle sprites and redraw in their new position (Note: Possibly redundant in the case of in place sorting algos)
    rect_group.empty()
    for i in range(len(sort_list)):
        #draw rectangles for every value in the list and screen flip. Rectangle height will corrospond to the value on the list. Rectangle width will corrospond to screen width/list amount
        rect_group.add(Rectangle(0 + screen_width/len(sort_list)*i , screen_height , screen_width/len(sort_list), sort_list[i], i , (255,0,0)))
    
    #update and display camera with the sorted rectangles
    camera.update()
    screen.blit(camera.image, camera.rect)
    pygame.display.update()
    
    #time delay after sorting
    time.sleep(1)
    
    #print to console the sort length and the total time it took for the function to complete sorting (without displaying to page)
    print(f"Instances: {len(sort_list)} Total Time: {total_time} seconds")
    
    #if the width of the rectangles become too small to be drawn individually on the screen (instances come close to the total amount of pixels displayed horizontally), they will not be displayed. In this case, break the loop
    if len(sort_list) == screen_width:
        break
    
    #event handler to close program
    for event in pygame.event.get():   
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()