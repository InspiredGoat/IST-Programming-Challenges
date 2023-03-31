import random

def bubbleSort(data):
    res = data
    loops = 0
    flipped = False

    while True:
        flipped = False

        #Loop through every item except for the last one
        for i in range(len(res)-1):

            #If the item is bigger than the one next to it, flip them
            if res[i] > res[i+1]:
                val = res[i]
                res[i] = res[i+1]
                res[i+1] = val
                flipped = True
        
        #If it hasn't flipped that means the array is sorted and we can return
        if not flipped:
            #Return the result and the number of loops
            return (res, loops)

        loops += 1


example = []

#Generate a random array
for i in range(100):
    example.append(random.randint(0, 100))

print("Example array: ")
print(example)

result = bubbleSort(example)

print("\nBubble sort result: ")
print(result[0])
print("in: " + str(result[1]) + " loops")