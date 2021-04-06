import random
# image of Rock , Paper and Scissor
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
    '''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
    '''

scissor = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
    '''
#values in the nested list here correspond to the above images
gameImages = [rock, paper, scissor]

#we get the user input and save it inside the userchoice variable
userChoice = int(input ("What do you choose? Type 0 for Rock, 1 for Paper or2 for Scissor\n"))

#check if it is greater than the intended range of value i.e. (not > 2)
#else it continue running it program as usual
if userChoice >= 3 or userChoice < 0:
    print ("You type the wrong number")
else:
    print (gameImages[userChoice]) #we input take the save value and insert it into the gameimage to form an index in it
    
    
    computerChoice = random.randint(0, 2)
    print ("Computer chose:")
    # we take the input from the computer random choice
    #and put it into gameImages to form an index of it with can be accessable
    print (gameImages[computerChoice])

    #Rock against scissor condition
    if userChoice == 0 and computerChoice ==2:
        print ("You win!")
    elif userChoice == 2 and computerChoice == 0:
        print ("You Lose")
        
    #if one of them is greater 
    elif computerChoice > userChoice:
        print ("Computer Win")
    elif userChoice > computerChoice:
        print ("You win")
        
    #Draw condition    
    elif computerChoice == userChoice:
        print("Draw")
