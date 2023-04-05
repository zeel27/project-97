import random 

print("number guessing game")
rand=random.randint(1,9)
chances=0
print("guess a number (1-9)")
while chances<5: 
      guess=int(input("enter your guess"))
      if guess==rand:
            print("congratulations you guessed that right")
      else :
            print("try another number")

      chances=chances+1 

if not chances<5:
    print("you lose the number is : ",rand)