import random

class Sorter:
    def __init__(self):
        self.myList = []

    def addNum(self, num):
        self.myList.append(num)

    def printList(self):
        print(self.myList)

    # Function to do insertion sort 
    def insertionSort(self): 

        for i in range(1, len(self.myList)): 

            x = self.myList[i] 

            j = i-1
            while j >=0 and x < self.myList[j] : 
                    self.myList[j+1] = self.myList[j] 
                    j -= 1
            self.myList[j+1] = x 

    def shuffle(self): 
        random.shuffle(self.myList)

    def bubbleSort(self):
        listSize = len(self.myList) 
  
        
        for i in range(listSize-1): 
        
            for j in range(0, listSize-i-1): 
                if self.myList[j] > self.myList[j+1] : 
                    self.myList[j], self.myList[j+1] = self.myList[j+1], self.myList[j]

    def selectionSort(self):
        for i in range(len(self.myList)): 

            old_i = i 
            for j in range(i+1, len(self.myList)): 
                if self.myList[old_i] > self.myList[j]: 
                    old_i = j 
      
            self.myList[i], self.myList[old_i] = self.myList[old_i], self.myList[i] 


