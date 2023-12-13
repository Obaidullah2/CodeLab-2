#Exercise 5: Continue 
#Write a program that implements a while loop. This program should ask the user if they would like to continue and use the while loop to keep looping as long as they enter the letter Y. Once the while loop has terminated output the number of times it is executed.

#importing random library
import random

#counting the repitition of the loop
dice_rounds=0

#while loop will keep looping itself while it is True until it turns false or it breaks the loop with a conditon
while True:
    #incrementing the number of times the loops is repeated by 1 every time the loop is used
    dice_rounds+=1
    #printing a random integer ranging from 1 until 6 inside a variable called dice which will keep 
    dice=random.randint(1,6)
    print(dice)
    #asking user if they want another new number of the dice which will determine if the while loop should continue or break
    answer=input("\nRoll the dice?\nType 'y' if yes: ")
    #if user clicks y and continues then the while loop's condition stays true
    if answer=="y":
        continue
    #otherwise with break it will end the loop if the user inputs any other letter than y
    else:
        break

#after the loop ends it will display the number of times the loop was used
# it will show the total result after the loop is terminated
print("\nThe number of times the dice was rolled: ",dice_rounds)