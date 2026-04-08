def start_game():
    print("Welcome to the Adventure Game!")
    name = input("What is your name, adventurer? ")
    print(f"Hello, {name}! Your quest is to find the legendary treasure hidden in this ancient land.")
    print("You have two paths to choose from: a dark forest and a mysterious cave.")
    choice = input("Which path will you take? (forest/cave) ").lower()
    
    if choice == "forest":
        forest_path()
    elif choice == "cave":
        cave_path()
    else:
        print("Invalid choice. Please enter 'forest' or 'cave'.")
        start_game() 

def forest_path():
    print("You have chosen to explore the dark forest.")
    print("As you venture deeper into the forest, you encounter a fork in the path.")
    print("To your left, you hear the sound of flowing water.")
    print("To your right, you see a tall tree with sturdy branches.")
    choice = input("Do you want to follow the river or climb the tree? (river/tree) ").lower()
    
    if choice == "river":
        follow_river()
    elif choice == "tree":
        climb_tree()
    else:
        print("Invalid choice. Please enter 'river' or 'tree'.")
        forest_path()

def follow_river():
    print("You follow the river downstream, hoping it leads somewhere useful.")
    print("After a while, you discover an ancient stone arch near the riverbank.")
    print("Behind the arch, you spot the glimmer of gold!")
    print("Congratulations! You found the legendary treasure!")
    print("YOU WIN!")

def climb_tree():
    print("You climb high into the tall tree to get a better view of your surroundings.")
    print("From the top, you can see the entire forest and spot something shimmering in the distance.")
    print("You notice a hidden cave entrance at the base of a mountain across the forest.")
    print("You safely descend and make your way toward the mountain.")
    cave_path()

def cave_path():
    print("You have entered a mysterious cave.")
    print("The cave is dark and narrow. You can barely see ahead of you.")
    print("You find an old torch on the ground.")
    choice = input("Do you want to light the torch or proceed in the dark? (torch/dark) ").lower()
    
    if choice == "torch":
        print("You light the torch and illuminate the cave.")
        print("The light reveals a clear path and beautiful crystal formations.")
        print("You follow the path and discover a chamber filled with glowing crystals.")
        print("In the center, you find the legendary treasure chest!")
        print("Congratulations! YOU WIN!")
    elif choice == "dark":
        print("You decide to proceed without light, feeling your way along the cave wall.")
        print("After a few steps, you stumble and fall into a deep pit.")
        print("You tumble through darkness...")
        print("GAME OVER - You lost!")
    else:
        print("Invalid choice. Please enter 'torch' or 'dark'.")
        cave_path()

# Start the game
if __name__ == "__main__":
    play_again = True
    while play_again:
        start_game()
        restart = input("\nDo you want to play again? (yes/no) ").lower()
        if restart == "yes":
            play_again = True
            print("\n" + "="*50)
            print("Starting a new adventure...")
            print("="*50 + "\n")
        else:
            play_again = False
            print("\nThank you for playing the Adventure Game! Goodbye!")



