
#rock=1,paper=2,scissor=3
opt=[1,2,3]
import random
#    1 2 3
# 1  D L W
# 2  W D L
# 3  L W D
sol=[["Draw","Lose","Win"],["Win","Draw","Lose"],["Lose","Win","Draw"]]
print("Welome to Rock, Paper, Scissor")
play="Y"
while(play.upper()=="Y"):
    player_choice=int(input("Enter your choice \nRock=1,Paper=2,Scissor=3: "))
    comp_choice=random.choice(opt)
    if(sol[player_choice-1][comp_choice-1]=="Win"):
        print("You Won")
    elif(sol[player_choice-1][comp_choice-1]=="Lose"): 
        print("You Lose")
    else:
        print("Its a Draw")
    play=input("Want to play one more time (Y/N): ")
print("Thanks for playing!")


