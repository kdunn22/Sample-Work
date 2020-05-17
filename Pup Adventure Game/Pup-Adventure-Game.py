import graphics as g
import random 

print("Welcome to the Pup Adventure Game!")
userName = input("Please enter a name for your pup: ")

win= g.GraphWin("Pup Adventure Game",400,400)

pupName = g.Text( g.Point(200,25), userName)
pupName.draw(win)
pupImageFileName = "pup.gif"
pupImage = g.Image(g.Point(200,200), pupImageFileName)
pupImage.draw(win)
win.getMouse()
win.close()

print("{}, your goal is to get to the toy and treat chest while collecting as many buddy biscuits along the way!".format(userName))
print("If you collect at least 14 buddy biscuits, you'll get the toy and treat chest!")
print("Good luck pup, and watch out for enemies that hurt your puppy health!")

i = 0
pupHealth = 100
buddyBiscuits = 0

#These flags are used to check whether or not each encounter has been run
hFlag = 0
mFlag = 0
nFlag = 0

while i < 3:
    number = random.randint(1,3)
    # CONDITION 1
    if number == 1:
        if hFlag == 1:
            continue
        else:
            print("You wake up to a loud crash.")
            conditionInput = input("Do you get off the bed and walk 5 steps to investigate (y/n)? ")

            winName = "Morning"
            hFlag = 1
            
            if conditionInput == "y":
                pupHealth = pupHealth - 1
                condition = "OH NO! Hoagie the kitty attacks"
                imageFileName = "Hoagie.gif"
                statement = "Hoagie meows loudly at you. You lost 1 puppy health point. Puppy health at " + str(pupHealth) + "."
            else:
                buddyBiscuits = buddyBiscuits + 4
                condition = "Good pup! You get 4 buddy biscuits!"
                imageFileName = "buddy.gif"
                statement = "You have " + str(buddyBiscuits) + " buddy biscuits."
    
    # CONDITION 2 
    elif number == 2:
        if mFlag == 1:
            continue
        else:
            print("You see an open can of cat food on the floor.")
            conditionInput = input("Do you walk 4 steps ahead to get some of the cat food (y/n)? ")

            winName = "Cat Food"
            mFlag = 1

            if conditionInput == "y":
                pupHealth = pupHealth - 10
                condition = "OH NO! Mia the kitty attacks!"
                imageFileName = "Mia.gif"
                statement = "Mia hisses with all of her might. You lost 10 puppy health points." + "Puppy health at " + str(pupHealth) + "."
            else:
                buddyBiscuits = buddyBiscuits + 10
                condition = "Good pup! You get 10 buddy biscuits!"
                imageFileName = "buddy.gif"
                statement = "You have " +str(buddyBiscuits) + " buddy biscuits."

    else:
        # CONDITION 3
        if nFlag == 1:
            continue
        else:
            print("You see a cool looking cat toy on the ground.")
            conditionInput = input("Do you walk 7 steps to have some fun (y/n)? ")
            
            winName = "Cat Toy"
            nFlag = 1

            if conditionInput == "y":
                pupHealth = pupHealth - 15
                condition = "OH NO! Mean Mugee the kitty attacks"
                imageFileName = "Mugee.gif"
                statement = "Mugee scratches you. You lost 15 puppy health points. Puppy health at " + str(pupHealth) + "."
            else:
                buddyBiscuits = buddyBiscuits + 10
                condition = "Good pup! You get 10 buddy biscuits!"
                imageFileName = "buddy.gif"
                statement = "You have " + str(buddyBiscuits) + " buddy biscuits."

    print(condition)
    print(statement)
    
    win = g.GraphWin(winName, 400, 400)
    text = g.Text( g.Point(200,25), condition)
    text.draw(win)
    image = g.Image(g.Point(200,200), imageFileName)
    image.draw(win)
    win.getMouse()
    win.close()
    
    i = i + 1

#Total output statements
print("Pup Health = " + str(pupHealth))
print("Buddy Biscuits = " + str(buddyBiscuits))
if buddyBiscuits >= 14:
    print("Good job pup, you got the toy and treat chest!")
else:
    print("Sorry pup, no toy and treat chest for you.")