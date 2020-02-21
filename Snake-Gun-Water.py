# Snake_Gun_Water
import random
List = ("Gun","Water","Snake")
j = 0
m = 0

choice ={"g": "Gun","s":"Snake","w":"Water"}
for i in range(9):
    k = random.choice(List)

    Player_choice = input("Enter choice g for (gun), s for (water)or w for (snake):\n")


    if Player_choice == "g":
        print("Computer\'s choice: ", k)
        print("Player\'s choice: ",choice[Player_choice])
        if (Player_choice == "g") and (k == "Snake"):
            j = j+1
            print("You Win", (j))
            m = m-1
            print("Opponent Loss", (m))
        elif (Player_choice == "g") and (k == "Water"):
            j = j-1
            print("You Loss", "Your Point:",(j))
            m = m+1
            print("Opponent Win","Opponent Points", (m))
        elif (Player_choice == "g") and (k == "Gun") and (i != 0):
            print("Your Score remain", (j))
            print("Opponent Score remain", (m))
            print("Try Again")
        continue



    elif Player_choice == "s":
        print("Computer\'s choice: ", k)
        print("Player\'s choice: ", choice[Player_choice])
        if (Player_choice == "s") and (k == "Water"):
            j = j+1
            print("You Win", (j))
            m = m-1
            print("Opponent Loss", (m))
        elif (Player_choice == "s") and (k == "Gun"):
            j = j-1
            print("You Loss", (j))
            m = m+1
            print("Opponent Win", (m))
        elif (Player_choice == "s") and (k == "Snake") and (i != 0):
            print("Your Score remain", (j))
            print("Opponent Score remain", (m))
            print("Try Again")
        continue


    elif Player_choice == "w":
        print("Computer\'s choice: ", k)
        print("Player\'s choice: ", choice[Player_choice])
        if (Player_choice == "w") and (k == "Gun"):
            j = j+1
            print("You Win", (j))
            m = m-1
            print("Opponent Loss", (m))
        elif (Player_choice == "w") and (k == "Snake"):
            j = j-1
            print("You Loss", (j))
            m = m+1
            print("Opponent Win", (m))
        elif (Player_choice == "w") and (k == "Water") and (i != 0):
            print("Your Score remain", (j))
            print("Opponent Score remain", (m))
            print("Try Again")
        continue

    i = i+1

if j > m:
    print(":)Player Win With Point: ",j)
elif m > j:
    print("*_*Computer Win With Point: ",m)
else:
    print("Game Draw")

