import random
Team = ["CSK","MI","RCB","KKR","SRH","DC","RR","PBKS","LSG","GT"]
print("Teams are :",Team)
your_Team = int(input("Enter your team :"))
if your_Team in Team:
        print("You have selected :",Team)


opponent = random.choice(Team)
print("Your opponent is :",opponent)
