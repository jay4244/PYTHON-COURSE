import random

print("----------- IPL 2025 -------------")

Teams  =["CSK", "MI", "RCB", "KKR", "SRH", "DC", "PBKS", "LSG","GT","RR"]

print(Teams)

User_Team = input("Enter your Team Name: ")
if User_Team in Teams:
        print("Your Team is :", User_Team)

Opponent_Team = random.choice(Teams)
print("Your opponent is :", Opponent_Team)

print("----------- Toss Time -------------")

Toss = random.choice(["Heads", "Tails"])
User_Toss = input("Choose your Toss(H/T): ")

Actual_Toss = random.choice(["H", "T"])
if User_Toss == Actual_Toss:
        print("You are Won the Toss")
        user_Decision = input("Choose your Decision (Bat/Bowl): ")
        print("You have chosen to :", user_Decision)
else:
        print("you are lost the Toss")
        
print("----------- Match Start -------------")
print("Match between", User_Team, "and", Opponent_Team, "has started.")   
print("-------------------------------------")

Run_List = ["1","2","3","4","5","6","Wide","Noball","Wicket"]
print("Over 1:",end=" ")
for ball in range(1,7):
        Teams_Run = random.choice(Run_List)
        print("Team run is :",Teams_Run) 
        if Teams_Run == "Wicket":
                print("player is out")
                break
Total_Runs = ball + Teams_Run
print("Total Runs scored in Over 1 is :", Total_Runs)        