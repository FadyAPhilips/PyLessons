import time

def countdown(start, end = 0, sleepTime = 1):
    print("starting")
    for i in range(start, end, -1):
        print(i)
        time.sleep(sleepTime)
    totalWait = (start - end) * sleepTime
    print("Done")

    if(totalWait < 2):
        return 0

    print("hello")    
    return(totalWait)


grandTotal = 0
grandTotal += countdown(5, 3, 2)
grandTotal += countdown(10, 5, 1)
grandTotal += countdown(3, 0, 1)
grandTotal += countdown(1, 0, 1)

print("total countdown is: " + str(grandTotal))