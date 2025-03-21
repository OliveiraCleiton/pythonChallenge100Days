# day 03, project: Treasure Island
print("Welcomw to Treasure Island.")
print("Your mission is to find the treasure.")
print("You're at a cross road. Where do you want to go?")

direction = input("Type \"left\" or \"right\"\n")
if direction == "left":
    print("You've come to lake. There is a island in the middle of the lake.")
    action = input("Type \"wait\" to wait a boat. Type \"swim\" to swim across.\n")
    if action == "wait":
        print("You arrive at the island unharmed. There is a house with 3 doors.")
        color = input("One red, one yellow and one blue. Which color do you choose?\n")
        if color == "red":
            print("Burned by fire. Game Over.")
        elif color == "blue":
            print("Eaten by beats. Game Over.")
        else:
            print("You found the treasure. You win!!!")
    else:
        print("Attacked by trout. Game Over.")
else:
    print("You fall into a hole.")
    print("Game Over...")

