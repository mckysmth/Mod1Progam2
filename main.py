
from sorter import Sorter
def main():
    sorter = Sorter()

    userInput = None

    while userInput != "":
        userInput =input("[Enter '' to quit]: ")
        if userInput != "":
            sorter.addNum(userInput)

    print("\n")

    sorter.printList()

    print("\n")


    userInput = None
    while userInput != "":
        userInput =input("\n1. Insertion Sort \n2. Bubble Sort \n3. Selection Sort \n4. Shuffle \n> " )

        print("\nList before selection:")
        sorter.printList()  

        if userInput == "1":
            sorter.insertionSort()

        elif userInput == "2": 
            sorter.bubbleSort()

        elif userInput == "3": 
            sorter.selectionSort()

        elif userInput == "4":
            sorter.shuffle()

        elif userInput != "":
            print("invalid command")
        
        print("\nList before selection:")
        sorter.printList()
        

    
    

if __name__ == "__main__":
    main()