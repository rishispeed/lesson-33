def space_explorer():
    print("you have crash landed on Mars, Now you have to survive")
    
    choice1=input("go to cave or forrest     ").lower()

    if choice1 == "cave":
        if input(("you havefound to pick up glowing stone (yes/no): ")).lower()=="yes":
              print("you found the light and survived")
        
        else:
             print("A monster appeared, game over,")
    elif choice1=="forrest":
         choice2=input("Follow the sound or clib a tree? (follow/climb): ").lower()
         if choice2 == "climb":
              print("you climed the tree and have found your ship! you survived.")
         else:
              print("Aliens surrounded you, Game over")
    else:
         print("You ran out of oxygen Game over")
    
space_explorer()


             

