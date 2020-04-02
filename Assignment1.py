import random

def main():
    n = int(input("Please enter a number less than 10 and more than 3\n"))

    while(n>9 or n <4):
        n = int(input("Please enter a number less than 10 and more than 3\n"))

    else:
        placement = []

        for i in range(n):
            placement.append(random.randrange(1,n+1))

    print("This is the board at the start:")
    print("".join(map(str, placement)))
    print()
    iterationCount = 1
    conflicts = checkConflicts(placement)
    localMaxima= False
    while(conflicts!=0 and not localMaxima):
        placement = placeQueen(placement,n)
        conflicts=checkConflicts(placement)
        print("This is the board after " + str(iterationCount) + " iterations:")
        print("".join(map(str, placement)))
        print()
        iterationCount+=1
        if(iterationCount>100):
            localMaxima=True
    if(localMaxima):
        print("A local maxima was hit.  Please try again\n")
        main()


# This function checks how many conflicts there are with a given board placement
# It returns the amount of conflicts there are
def checkConflicts(placement):
        n = len(placement)
        sum =0
        for col in range(0,n):
            for row in range(col+1,n):
                if placement[col]==placement[row]:
                    sum+=1
                elif (int(placement[col])+row-col)==int(placement[row]):
                    sum+=1
                elif (int(placement[col])-row+col)==int(placement[row]):
                    sum += 1
        return sum

# This checks individual rows for their conflicts.  I implemented it a different way and it is no longer necessary

        #
        # for j in range(indexBeingEvaluated+1,n):
        #         if placement[indexBeingEvaluated]==placement[j]:
        #             sum+=1
        #             print("got here")
        #         elif (int(placement[j])+j-indexBeingEvaluated)==int(placement[indexBeingEvaluated]):
        #             sum+=1
        #             print("got here 2")
        #         elif (int(placement[j])-j+indexBeingEvaluated)==int(placement[indexBeingEvaluated]):
        #             sum += 1
        #             print("got here 3")


# This function moves a queen in the position with the lowest heuristic

def placeQueen(placement,n):

    moveList={}
    for col in range(0,n):
        for row in range(1,n+1):
            if placement[col]==row:
                continue
                # continues on to the next iteration of the loop
            newPlacement= placement.copy()
            newPlacement[col]=row

            # This creates a new board placement and then puts the row and column value in a dictionary along with the amount of conflicts are associated with the position

            moveList[(col,row)] = checkConflicts(newPlacement)
    # bestHeuristic is the best heuristic value we have so far.  It gets updated when a lower value is found
    bestHeuristic = checkConflicts(placement)

    lowestHeuristic= []
    for i,h in moveList.items():
        if h<bestHeuristic:
            # Checks the value of the dictionary keys and assigns the value to bestHeuristic if it's lower than the current bestHeuristic value
            bestHeuristic=h
    for i,h in moveList.items():
        if h==bestHeuristic:
            # appends to the lowestHeuristic list if the value of the key equals the bestHeuristic value
            lowestHeuristic.append(i)

    # This if statement only runs if lowestHeuristic has been appended to.  It picks a random number to evaluate

    if len(lowestHeuristic)>0:
        randomNum = random.randint(0,len(lowestHeuristic)-1)
        col = lowestHeuristic[randomNum][0]
        row=lowestHeuristic[randomNum][1]
        placement[col]=row
    return placement
main()
