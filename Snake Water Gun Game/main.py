import random

# Snake-Water-Gun: 1 = Snake, -1 = Water, 0 = Gun
youDict = {"s": 1, "w": -1, "g": 0}
reverseDict = {1: "Snake", -1: "Water", 0: "Gun"}

your_score = 0
computer_score = 0
rounds = 0
total_rounds = 3

while rounds < total_rounds:
    computer = random.choice([-1, 0, 1])
    youstr = input("\nEnter your choice: ").lower()

    if youstr == 'q':   #Ends the game at any round according to the user.
        break

    if youstr not in youDict:
        print("Invalid input. Please enter 's', 'w', or 'g'.")  
        continue

    you = youDict[youstr]

    print(f"You chose {reverseDict[you]}")
    print(f"Computer chose {reverseDict[computer]}")

    if computer == you:
        print("It's a draw!")

    elif (computer == -1 and you == 1) or (computer == 1 and you == 0) or (computer == 0 and you == -1):
        print("You win this round!")
        your_score += 1

    else:
        print("Computer wins this round!")
        computer_score += 1

    rounds += 1
    print(f"Your Score : {your_score}  \nComputer Score: {computer_score}")

#total_rounds stops the at 5 rounds. 

print("\nGame Over!")
print(f"Total Rounds Played: {total_rounds}")
print(f"Your Final Score: {your_score} \nComputer's Final Score: {computer_score}")

if your_score > computer_score:
    print("Congratutions, You won the game!")
elif your_score < computer_score:
    print("Awwwwww, Computer won the game. Better luck next time.")
else:
    print("The game is a draw.")
