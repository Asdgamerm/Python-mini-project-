computer = -1
youstr = input("Enter your choice ")
youDict = {"R": 1, "P": -1, "S": 0}
reverseDict = {1: "Rock", -1:"paper", 0: "Scissors"}

you = youDict[youstr]

print(f"you chose {reverseDict[you]}\nComputer choice {reverseDict[computer]}")

if (computer == you ):
    print("It's a Draw")
else:
    if(computer == -1 and you == 1 ):
        print("You Win")
    elif(computer == -1 and you == 0):
        print("You lose!")
    elif(computer == 1 and you == 0):
        print("You Win ")
    elif(computer == 1 and you == -1):
        print("You Lose")
    elif(computer == 0 and you == 1):
        print("You win")
    elif(computer == 0 and you == -1):
        print("You Lose!")
    else:
        print("Something went Wrong")