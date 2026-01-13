Quiz ={
    1 :{
        "que" : "Which language is most popular ?",
        "ans" : "python",
    },
    2 :{
        "que" : "Who is prime minister of india ?",
        "ans" : "modi",
    },
    3 :{
        "que" : "most popular cricketer ?",
        "ans" : "dhoni"
    },
}

#print(Quiz)
#print(Quiz[1]["que"])
score =0
for i in range(1,len(Quiz)+1):
    print(f"Que. ({i}) {Quiz[i]["que"]}")
    ans = input("Enter your answer : ")
    if ans==Quiz[i]["ans"]:
        score+=1
        print("correct answer")
    else:
        score-=1
        print("wrong answer")
            
    