# Hi its Deepak Pandey again

import random
List = ("Gun","Water","Snake")
j = 0
m = 0
n = 10
player ={"g": "Gun","s":"Snake","w":"Water"}

for i in range(1,n+1):
    k = random.choice(List)

    Player_choice = input("Enter choice g for (gun), s for (water)or w for (snake):\n")


    if Player_choice == "g":
        print("Computer\'s choice: ", k)
        print("Player\'s choice: ",player[Player_choice])
        if (Player_choice == "g") and (k == "Snake"):
            j = j+1
            print("Your point", j)
            m = m-1
            print("Opponent point", m)
            n = n -1
            print("Life Left", n)
        elif (Player_choice == "g") and (k == "Water"):
            j = j-1
            print("Your Point: ",(j))
            m = m+1
            print("Opponent Points: ", (m))
            n = n - 1
            print("Life Left", n)
        elif (Player_choice == "g") and (k == "Gun") and (i != 0):
            print("Your Score remain", (j))
            print("Opponent Score remain", (m))
            n = n - 1
            print("Life Left", n)
            print("Try Again")

        continue



    elif Player_choice == "s":
        print("Computer\'s choice: ", k)
        print("Player\'s choice: ", player[Player_choice])
        if (Player_choice == "s") and (k == "Water"):
            j = j+1
            print("Your Point: ", (j))
            m = m-1
            print("Opponent Points: ", (m))
            n = n - 1
            print("Life Left", n)
        elif (Player_choice == "s") and (k == "Gun"):
            j = j-1
            print("Your Point: ", (j))
            m = m+1
            print("Opponent Points: ", (m))
            n = n - 1
            print("Life Left", n)
        elif (Player_choice == "s") and (k == "Snake") and (i != 0):
            print("Your Score remain", (j))
            print("Opponent Score remain", (m))
            n = n - 1
            print("Life Left", n)
            print("Try Again")
        continue


    elif Player_choice == "w":
        print("Computer\'s choice: ", k)
        print("Player\'s choice: ", player[Player_choice])
        if (Player_choice == "w") and (k == "Gun"):
            j = j+1
            print("Your Point: ", (j))
            m = m-1
            print("Opponent Points: ", (m))
            n = n - 1
            print("Life Left", n)
        elif (Player_choice == "w") and (k == "Snake"):
            j = j-1
            print("Your Point: ", (j))
            m = m+1
            print("Opponent Points: ", (m))
            n = n - 1
            print("Life Left", n)
        elif (Player_choice == "w") and (k == "Water") and (i != 0):
            print("Your Score remain", (j))
            print("Opponent Score remain", (m))
            n = n - 1
            print("Life Left", n)
            print("Try Again")
        continue

    i = i+1

if j > m:
    print(":)Player Win With Point: ",j)
elif m>j:
    print("*_*Computer Win With Point: ",m)
else:
    print("Game Draw")
