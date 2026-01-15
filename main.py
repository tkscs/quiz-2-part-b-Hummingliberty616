current_state = "Forest"
while True:
    if current_state == "Forest":
        current_input = ("You can go north (N) or go east (E). " \
        "Which way would you like to go?")

    if current_state == "River":
        current_input = ("You can return to the forest (R) or swim (S)."
        "Which would you like to do?")
    
    if current_state == "Win":
        print("Congratulations! You won.")
        break

    if current_state == "Lose":
        print("Sorry, you have lost.")
        break
    
    if current_state == "Forest":
        if current_input == "N":
            current_state = "Win" 
        elif current_input == "E":
            current_state = "River"
    
    if current_state == "River":
        if current_input == "R":
            current_state = "Forest"
        elif current_input == "Swim":
            current_state = "Lose"
    