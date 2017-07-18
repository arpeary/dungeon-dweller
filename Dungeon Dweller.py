###########################################

# Title

def start(state):
    """(0.22 - alec) prints title + asks to begin/instruct/exit"""
#############################################################################
#   Programmer Name: Alec Perry					            #	    
#   Date: 12/7/16							    #
#   Purpose: To allow the player to purchase items with their gold	    #
#   Input: gp, inv							    #
#   Output: gp, inv							    #
#############################################################################

    # Color
    os.system("color 0C")
    open1 = open("titlescreen.txt", "r")
    open2 = open("instructscreen.txt", "r")
    open3 = open("credits.txt", "r")
    open4 = open("gameover.txt", "r")
    title = open1.read()
    instruct = open2.read()
    credit = open3.read()
    gameover = open4.read()
    state2= 0
    choice = 0

    while 1==1:
        if state == 4 or state2 == 4:
            while 1==1:
                os.system('cls')
                print(title)
                try:
                    choice = int(input())
                except:
                    ValueError
                if choice == 1:
                    begin = 1
                    return 1
                elif choice == 2:
                    os.system('cls')
                    print(instruct)
                    input("Press the 'Enter' key to return to title screen.")
                    continue
                elif choice == 3:
                    os.system('cls')
                    print(credit)
                    input("")
                    exit()
                    return
        elif state == 0:
            os.system('cls')
            input(gameover)
            os.system('cls')
            input(credit)
            exit()
            
############################################

# PICKLE FUNCTIONS

def list_to_pickle(the_file, the_list):
    """Converts a list to pickle"""
#############################################################################
#   Programmer Name: Peyton Davis					    #	    
#   Date: 12/10/16							    #
#   Purpose: Converts a list to a pickle                        	    #
#   Input: The file name and the List					    #
#   Output: The pickled file					    	    #
#############################################################################
    f = open_file(the_file, "wb")
    pickle.dump(the_list, f)
    f.close()

def pickle_to_list(the_file):
    """Converts a pickle to a list"""
#############################################################################
#   Programmer Name: Peyton Davis					    #	    
#   Date: 12/10/16							    #
#   Purpose: Converts a picle to a list                            	    #
#   Input: The file name			                	    #
#   Output: The list    					    	    #
#############################################################################
    f = open_file(the_file, "rb")
    newList = pickle.load(f)
    f.close()
    return newList

###########################################

# SWITCH MAP

def open_file(file_name, mode):
    """Opens a file and checks for exceptions to prevent errors"""
#############################################################################
#   Programmer Name: Peyton Davis					    #	    
#   Date: 12/8/16							    #
#   Purpose: Opens a file with an exception                            	    #
#   Input: The file name and the mode you want to oepn		    	    #
#   Output: The file    					    	    #
#############################################################################
    try:
        the_file = open(file_name, mode)
    except IOError as e:
        print("Unable to open the file", the_file , "Ending the program.\n", e)
        input("\n\nPress the enter key to exit.")
        sys.exit()
    else:
        return the_file

def count_map(the_file):
    """Finds the number of avaliable maps" and returns them to a list"""
#############################################################################
#   Programmer Name: Peyton Davis					    #	    
#   Date: 12/7/16							    #
#   Purpose: Gets a count of all the maps                            	    #
#   Input: The file of maps                     		    	    #
#   Output: A list of possible maps    					    #
#############################################################################
    f = open_file(the_file, "r")
    lines = f.readlines()
    map_list = []
    # Takes numbers that divide map numbers and
    # --- Put them in a list
    for line in lines:
        if not "#" in line:
            map_list.append(line[0])
    f.close()
    del map_list[len(map_list) - 1]
    return map_list

def choose_map(previous_map, map_list):
#############################################################################
#   Programmer Name: Peyton Davis					    #	    
#   Date: 12/6/16							    #
#   Purpose: Picks a random map                                     	    #
#   Input: The precious map and the list of maps		    	    #
#   Output: The current map number 					    #
#############################################################################
    """Chooses the next map for the game"""
    map_number = random.choice(map_list)
    while map_number == previous_map:
        map_number = random.choice(map_list)
    return map_number

def load_map(the_file, map_number):
#############################################################################
#   Programmer Name: Peyton Davis					    #	    
#   Date: 12/5/16							    #
#   Purpose: Converts the current map to a text file                        #
#   Input: The file you want to load the curernt map to and number 	    #
#   Output: The text file of the current map     			    #
#############################################################################
    """This loads in the new map and wrties it to a file by taking a slice"""
    f = open_file(the_file, "r")
    lines = f.readlines()
    for line in lines:
        if line[0] == str(map_number):
            start = (lines.index(line) + 1)
    # Removes slice before map
    del lines[:start]
    for line in lines:
        if line[0] == str(int(map_number) + 1):
            finish = lines.index(line)
    # Removes slice after map
    del lines[finish:]
    w = open_file("current_map.txt", "w+")
    w.writelines(lines)
    w.close()
    f.close()

def file_to_list(the_file):
#############################################################################
#   Programmer Name: Peyton Davis					    #	    
#   Date: 12/8/16							    #
#   Purpose: Converts a file to a list that can  used                       #
#   Input: The file 		    	                                    #
#   Output: The list    					    	    #
#############################################################################
    """Converts a textfile to a map"""
    f = open_file(the_file, "r")
    lines = f.readlines()
    f.close()
    return lines

def switch_map(the_file):
#############################################################################
#   Programmer Name: Peyton Davis					    #	    
#   Date: 12/5/16							    #
#   Purpose: Changes the current                                    	    #
#   Input: The file needed for the functions within it		    	    #
#   Output: The current_map file, but changed           	    	    #
#############################################################################
    """Switches the map and is complied"""
    map_list = count_map(the_file)
    map_num = choose_map(random.choice(map_list), map_list)
    load_map(the_file, str(map_num))

####################################################

# MOVE

def find_item(the_file, item):
#############################################################################
#   Programmer Name: Peyton Davis					    #	    
#   Date: 12/11/16							    #
#   Purpose: Finds the row and cloumn of an obejct in a file                #
#   Input: The file you want to search and the item you want to find	    #
#   Output: The row and cloumn of the object    			    #
#############################################################################
    """Gets the position of a item and returns the row and column"""
    lines = file_to_list(the_file)
    # Finds Row
    for line in lines:
        if item in line:
            row = lines.index(line)
        # Finds Columns
        for char in line:
            if char == item:
                column = line.index(char)
                return [row, column]
    

def try_pos(position, direction):
#############################################################################
#   Programmer Name: Peyton Davis					    #	    
#   Date: 12/9/16							    #
#   Purpose: Tries a positon to see if it is valid before the move is made  #
#   Input: The positon of the character and the direction they are facing   #
#   Output: The possible location  					    #
#############################################################################
    """Trys the postion"""
    try_pos = position
    if direction == "w":
        try_pos[0] = (position[0] - 1)
    if direction == "s":
        try_pos[0] = (position[0] + 1)
    if direction == "a":
        try_pos[1] = (position[1] - 1)
    if direction == "d":
        try_pos[1] = (position[1] + 1)
    return try_pos
    
    

def check_move(the_file, direction):
#############################################################################
#   Programmer Name: Peyton Davis					    #	    
#   Date: 12/10/16							    #
#   Purpose: Checks to see if the move can acutally be made                 #
#   Input: The file you want to check and teh direction the player is facing#
#   Output: If the move is valid or not    				    #
#############################################################################
    """Checks to see if a move is ok or not"""
    player_pos = find_item(the_file, "@")
    check_pos = try_pos(player_pos, direction)
    lines = file_to_list(the_file)
    INVALID_SPACES = ["#", "M", "[", "]"]
    for item in INVALID_SPACES:
        if lines[check_pos[0]][check_pos[1]] == item:
            return "not ok"
    return "ok"

def remove_player(the_file, player_pos):
#############################################################################
#   Programmer Name: Peyton Davis					    #	    
#   Date: 12/11/16							    #
#   Purpose: Removes the players character from the map                     #
#   Input: The file you want to edit and the players postion    	    #
#   Output: The edited text file    					    #
#############################################################################
    """Removes the player's charater from the map"""
    lines = file_to_list(the_file)
    f = open_file(the_file, "w")
    line_num = len(lines)
    for line in range(line_num):
        if line == player_pos[0]:
            rebuilt_line = []
            for char in lines[line]:
                rebuilt_line.append(char)
            rebuilt_line[player_pos[1]] = "."
            new_line = ""
            for char in rebuilt_line:
                new_line += char
            f.write(new_line)
        else:
            f.write(lines[line])
    f.close()
    
def add_player(the_file, player_pos):
#############################################################################
#   Programmer Name: Peyton Davis					    #	    
#   Date: 12/11/16							    #
#   Purpose: Adds the player to the new location on the map                 #
#   Input: The file you want to edit and the players positon    	    #
#   Output: The edited text file    					    #
#############################################################################
    """Adds the player to the new lcoation on the map"""
    lines = file_to_list(the_file)
    f = open_file(the_file, "w")
    line_num = len(lines)
    for line in range(line_num):
        if line == player_pos[0]:
            rebuilt_line = []
            for char in lines[line]:
                rebuilt_line.append(char)
            rebuilt_line[player_pos[1]] = "@"
            new_line = ""
            for char in rebuilt_line:
                new_line += char
            f.write(new_line)
        else:
            f.write(lines[line])
    f.close()

def update_map(the_file, direction):
#############################################################################
#   Programmer Name: Peyton Davis					    #	    
#   Date: 12/10/16							    #
#   Purpose: Removes the player and adds the player back                    #
#   Input: The file you want to edit and the direction of tje player	    #
#   Output: The edited text file    					    #
#############################################################################
    """rewrites the map because the players move is valid"""
    pos = find_item(the_file, "@")
    remove_player(the_file, pos)
    player_pos = try_pos(pos, direction)
    add_player(the_file, player_pos)

def test_area(the_file, position, invalid_spaces):
#############################################################################
#   Programmer Name: Peyton Davis					    #	    
#   Date: 12/11/16							    #
#   Purpose: Tests the area aroudnd an object                               #
#   Input: The file, the postion of the player, and teh spaces considered   #
#          invalid                                                          #
#   Output: If the area is clear or not     				    #
#############################################################################
    """Tests the area around and obeject"""
    lines = file_to_list(the_file)
    state = 0
    AREA = [[1,1], [1,0], [1, -1], [-1, 1], [-1,0], [-1, -1],[0, 1], [0,-1], [0,0]]
    for pos in AREA:
        position[0] += pos[0]
        position[1] += pos[1]
        for item in invalid_spaces:
            if lines[position[0]][position[1]] == item:
                state = 1
        position[0] -= pos[0]
        position[1] -= pos[1]
    return state

def remove_monster(the_file, position, invalid_spaces):
#############################################################################
#   Programmer Name: Peyton Davis					    #	    
#   Date: 12/12/16							    #
#   Purpose: Removes the mosnter after you fight it                         #
#   Input: The file you want to edit, the possition and invalid spaces	    #
#   Output: The edited text file    					    #
#############################################################################
    """Removes the mosnter after you fight it"""
    lines = file_to_list(the_file)
    state = 0
    AREA = [[1,1], [1,0], [1, -1], [-1, 1], [-1,0], [-1, -1],[0, 1], [0,-1], [0,0]]
    for pos in AREA:
        position[0] += pos[0]
        position[1] += pos[1]
        for item in invalid_spaces:
            if lines[position[0]][position[1]] == item:
                state = position
                remove_player(the_file, position)
        position[0] -= pos[0]
        position[1] -= pos[1]
    
def write_door_part(the_file, pos):
#############################################################################
#   Programmer Name: Peyton Davis					    #	    
#   Date: 12/12/16							    #
#   Purpose: Writes the open door animation to the map                      #
#   Input: The file you want to edit and positon of the door    	    #
#   Output: The edited text file    					    #
#############################################################################
    """Writes door part to map when player has key; opens door animation"""
    lines = file_to_list(the_file)
    f = open_file(the_file, "w")
    for line in range(0, len(lines)):
        if line == pos[0]:
            line = str(lines[line])
            new_line = []
            for char in range(len(line)):
                if line[char] == "[":
                    new_line.append("[")
                    new_line.append(" ")
                    new_line.append(" ")
                else:
                    new_line.append(line[char])
            rebuilt_line = ""
            for char in new_line:
                rebuilt_line += char        
            rebuilt_line = rebuilt_line[2:]
            f.write(rebuilt_line)
        else:
            f.write(lines[line])
    f.close()

def update_door(the_file):
#############################################################################
#   Programmer Name: Peyton Davis					    #	    
#   Date: 12/12/16							    #
#   Purpose: Finds the door in the map and aniamtes the opening             #
#   Input: The file you want to edit with the door              	    #
#   Output: The edited text file    					    #
#############################################################################
    """Finds the door in the map and aniamtes the opening"""
    location = find_item(the_file, "[")
    write_door_part(the_file, location)

def door_cords(the_file):
#############################################################################
#   Programmer Name: Peyton Davis					    #	    
#   Date: 12/12/16							    #
#   Purpose: Finds the door in the map in terms of row and column           #
#   Input: The file you want to search with the door              	    #
#   Output: The coordinates of the door    				    #
#############################################################################
    """Finds the door in the map in terms of row and column"""
    door = []
    door_cords = find_item(the_file, "[")
    door_location = [[0, 1], [0, 2]]
    for item in door_location:
        door_new = [door_cords[0] + item[0], door_cords[1] + item[1]]
        door.append(door_new)
    return door

def add_key(the_file):
#############################################################################
#   Programmer Name: Peyton Davis					    #	    
#   Date: 12/12/16							    #
#   Purpose: Adds the key to players inventory if all the monsters are gone #
#   Input: The file you want to search for Monsters              	    #
#   Output: The state if the player needs the key     			    #
#############################################################################
    """Adds the key to players inventory if all the monsters are gone"""
    lines = file_to_list(the_file)
    state = 0
    for line in lines:
        if "M" in line:
            state = 1
    return state
            
def move(the_file, inventory_file, stats_file, monster_stats_file, level):
#############################################################################
#   Programmer Name: Peyton Davis					    #	    
#   Date: 12/12/16							    #
#   Purpose: All aspects that area reaquired to make a movement             #
#   Input: The file you want to edit, the player's stats, the player's      #
#          inventory, monster's stats,a dn teh current level                # 
#   Output: The move and the gui for             			    #
#############################################################################
    """Allows the player to move around the map"""
    player_inventory = pickle_to_list(inventory_file)
    player_stats = pickle_to_list(stats_file)
    health = player_stats[0]
    direction = "W"
    complete = 0
    door_state = 0
    printmove(the_file, health, player_inventory, direction, level, door_state)
    while complete != 1:

        # Trigger/Check Monster encounter
        player_inventory = pickle_to_list(inventory_file)
        player_stats = pickle_to_list(stats_file)
        health = player_stats[0]
        if test_area(the_file, find_item(the_file, "@"), "M") == 1:
            game_state = combat(inventory_file, stats_file, monster_stats_file, door_state)
            player_inventory = pickle_to_list(inventory_file)
            os.system('cls')
            if game_state == 0:
                start(0)
            else:
                remove_monster(the_file, find_item(the_file, "@"), "M")
                printmove(the_file, health, player_inventory, direction, level, door_state)
            
        # If player doesn't have key
        if add_key(the_file) == 0 and door_state == 0:
            player_inventory.append("Key")

        # Open Door
        if "Key" in player_inventory:
            update_door(the_file)
            player_inventory.remove("Key")
            door_state = 1
            
        choice = input()
        if choice != "":          
            direction = choice
        if choice == "":
            if check_move(the_file, direction) == "ok":
                    update_map(the_file, direction)

        # Check to see if player has completed level
        for cord in door_cords(the_file):
            if cord == find_item(the_file, "@"):
                complete = 1
        os.system('cls')
        printmove(the_file, health, player_inventory, direction, level, door_state)
        list_to_pickle(inventory_file, player_inventory)
    list_to_pickle(inventory_file, player_inventory)
    return 1

    
#########################################################

# Monsters

def add_monsters(the_file, monster_stats_file):
#############################################################################
#   Programmer Name: Peyton Davis					    #	    
#   Date: 12/12/16							    #
#   Purpose: Adds monsters to the map                                       #
#   Input: The file you want to add them too and the monster's stats        #
#   Output: The monsters on the map             			    #
#############################################################################
    """Adds monsters to the map"""
    lines = file_to_list(the_file)
    moster_stats = pickle_to_list(monster_stats_file)
    monster_count = monster_stats[0]  
    num_of_monsters = random.choice(monster_count)
    while num_of_monsters != 0:
        row = random.randint(1, (len(lines)-2))
        column = random.randint(1, (len(lines[0])-2))
        possiable_pos = [row, column]
        if test_area(the_file, possiable_pos, ["#", "@", "M"]) == 0:
            write_monster(the_file, possiable_pos)
            num_of_monsters -= 1
        else:
            continue

def write_monster(the_file, pos):
#############################################################################
#   Programmer Name: Peyton Davis					    #	    
#   Date: 12/12/16							    #
#   Purpose: Physically writes the monsters to the text file to be printed  #
#   Input: The file you want to add them to and the positon                 #
#   Output: The edited text file                 			    #
#############################################################################
    """Writes monster to map"""
    lines = file_to_list(the_file)
    f = open_file(the_file, "w")
    line_num = len(lines)
    for line in range(line_num):
        if line == pos[0]:
            rebuilt_line = []
            for char in lines[line]:
                rebuilt_line.append(char)
            rebuilt_line[pos[1]] = "M"
            new_line = ""
            for char in rebuilt_line:
                new_line += char
            f.write(new_line)
        else:
            f.write(lines[line])
    f.close()
            
def update_difficulty(monster_stats_file):
#############################################################################
#   Programmer Name: Peyton Davis					    #	    
#   Date: 12/12/16							    #
#   Purpose: Increases monster occurences, health, and damage               #
#   Input: The monster's stats                                    	    #
#   Output: The edited monster stats             			    #
#############################################################################
    monster_stats = pickle_to_list(monster_stats_file)
    for i in range(0,4):
        monster_stats[0][i] += 1
    for i in range(1,3):
        monster_stats[1][i] += .5
    for i in range(0,4):
        monster_stats[2][i] += 1
    list_to_pickle(monster_stats_file, monster_stats)
    
#########################################################

# COMBAT

def combat(inventory_file, stats_file, monster_stats_file, door_state):
#############################################################################
#   Programmer Name: Jared Janak , Alec Perry                               #
#   Date: 12-10/16                                                          #
#   Purpose: To run through an enemy encounter                              #
#   Input: hp, i, gp                                                        #
#   Output: gamestate for win or lose	                                    #
#############################################################################
    stats = pickle_to_list(stats_file)
    i = pickle_to_list(inventory_file)
    hp = stats[0]
    gp = stats[1]
    monster_stats = pickle_to_list(monster_stats_file)
    monster_health = random.choice(monster_stats[2])
    strength = 0
    defense = 0
    block = armor_rating(i)
    buffer=open("combatbuffer.txt", "r+")
    buffer.write("You have encountered a monster.\n"+"You have "+str(hp)+\
                 " health.\n")

    while monster_health > 0 and hp > 0:
        os.system('cls')
        printcombat(buffer,open("battle.txt", "r"))
        choice = input()
        open("combatbuffer.txt", 'w').close()

        if choice == "1":
            human_attack = sword_rating(i)
            if strength > 0:
                human_attack = int((human_attack)*1.5)
                strength-=1
            buffer.write("You attack the monster and deal "+str(human_attack)+\
                         " damage.\n")
            monster_health -= human_attack
            if monster_health > 0:
                buffer.write("The monster now has "+str(monster_health)+" health left\n")
                monster_attack = random.choice(monster_stats[1])
                if defense > 0:
                    monster_attack*=.5
                if monster_attack == 0:
                    buffer.write("The monster missed you!\n")
                else:
                    buffer.write("The monster attacks back and deals you "+\
                                     str(monster_attack)+" damage.\n")
                    buffer.write("Your armor blocks "+str(block)+" damage.\n")
                    if (monster_attack-block)< 0:
                        monster_attack= block
                    hp -= (monster_attack-block)
                if hp > 0:
                    buffer.write("You have "+str(hp)+" health left.\n")
                else:
                    buffer.write("You have no health left.\n")
            else:
                buffer.write("The monster has no health left.\n")
        
        elif choice == "2":
            heal,stre,defe=0,0,0
            for item in i:
                if item == "Healing":
                    heal+=1
                elif item == "Strength":
                    stre+=1
                elif item == "Defense":
                    defe+=1
            if heal > 0:
                buffer.write("1 - Healing Potion x"+str(heal)+"\n")
            if stre > 0:
                buffer.write("2 - Strength Potion x"+str(stre)+"\n")
            if defe > 0:
                buffer.write("3 - Defense Potion x"+str(defe)+"\n")
            os.system('cls')
            printcombat(buffer,open("potions.txt","r"))
            c2=input("")
            if "Healing" in i and c2== "1":
                if hp == 20:
                    buffer.write("You're already at full health.\n")
                elif hp <= 10:
                    buffer.write("You use a Healing Potion and restore 10 health.\n")
                    hp += 10
                    i.remove("Healing")
                    monster_attack = random.choice(monster_stats[1])
                    if defense > 0:
                        monster_attack*=.5
                    if monster_attack == 0:
                        buffer.write("The monster missed you!\n")
                    else:
                        buffer.write("The monster attacks back and deals you "+\
                                     str(monster_attack)+" damage.\n")
                        buffer.write("Your armor blocks "+str(block)+" damage.\n")
                        if (monster_attack-block)< 0:
                            monster_attack= block
                        hp -= (monster_attack-block)
                    if hp > 0:
                        buffer.write("You have "+str(hp)+" health left.\n")
                    else:
                        buffer.write("You have no health left.")    
       
                elif hp < 20 and hp > 10:
                    health_plus = (20 - hp)
                    buffer.write("You use a Healing Potion and restore ")
                    buffer.write(str(health_plus))
                    buffer.write(" health.\n")
                    hp += health_plus
                    i.remove("Healing")
                    monster_attack = random.choice(monster_stats[1])
                    if defense > 0:
                        monster_attack*=.5
                    if monster_attack == 0:
                        buffer.write("The monster missed you!\n")
                    else:
                        buffer.write("The monster attacks back and deals you "+\
                                     str(monster_attack)+" damage.\n")
                        buffer.write("Your armor blocks "+str(block)+" damage.\n")
                        if (monster_attack-block)< 0:
                            monster_attack= block
                        hp -= (monster_attack-block)
                    if hp > 0:
                        buffer.write("You have "+str(hp)+" health left.\n")
                    else:
                        buffer.write("You have no health left.\n")    

            elif "Strength" in i and c2== "2":
                strength=5
                i.remove("Strength")
                buffer.write("You use a Strength Potion and feel its energy take effect.\n")
                monster_attack = random.choice(monster_stats[1])
                if defense > 0:
                    monster_attack*=.5
                if monster_attack == 0:
                    buffer.write("The monster missed you!\n")
                else:
                    buffer.write("The monster attacks back and deals you "+\
                                 str(monster_attack)+" damage.\n")
                    buffer.write("Your armor blocks "+str(block)+" damage.\n")
                    if (monster_attack-block)< 0:
                        monster_attack= block
                    hp -= (monster_attack-block)
                if hp > 0:
                    buffer.write("You have "+str(hp)+" health left.\n")
                else:
                    buffer.write("You have no health left.\n")                    
            elif "Defense" in i and c2== "3":
                defense=5
                i.remove("Defense")
                buffer.write("You use a Defense Potion and feel its energy take effect.\n")
                monster_attack = random.choice(monster_stats[1])
                if defense > 0:
                    monster_attack*=.5
                if monster_attack == 0:
                    buffer.write("The monster missed you!\n")
                else:
                    buffer.write("The monster attacks back and deals you "+\
                                 str(monster_attack)+" damage.\n")                   
                    buffer.write("Your armor blocks "+str(block)+" damage.\n")
                    if (monster_attack-block)< 0:
                        monster_attack= block
                    hp -= (monster_attack-block)
                if hp > 0:
                    buffer.write("You have "+str(hp)+" health left.\n")
                else:
                    buffer.write("You have no health left.\n")    
            else:
                buffer.write("You don't have any of those Potions.\n")
                
        elif choice == "i":
            os.system('cls')
            printinventory(i, gp)
            input("")
            buffer.write("You stop looking in your bag.\n")
            buffer.write("The monster looks at you oddly.\n")
        else:
            buffer.write("You don't know what to do and hesitate!\n")
            monster_attack = random.choice(monster_stats[1])
            if defense > 0:
                monster_attack*=.5
            if monster_attack == 0:
                    buffer.write("The monster missed you!\n")
            else:
                buffer.write("The monster attacks back and deals you "+\
                             str(monster_attack)+" damage.\n")
                buffer.write("Your armor blocks "+str(block)+" damage.\n")
                if (monster_attack-block)< 0:
                     monster_attack= block
                hp -= (monster_attack-block)
            if hp > 0:
                buffer.write("You have "+str(hp)+" health left.\n")
            else:
                buffer.write("You have no health left.\n")
            
                    
    if monster_health <= 0:
        drop = random.randint(20, 40)
        gp += drop
        key_drp = key_drop(i, door_state)
        buffer.write("You have defeated the monster!\n")
        buffer.write("It dropped "+str(drop)+" gold!\n")
        buffer.write("You now have " +str(gp) + " gold!\n") 
        if key_drp == 1:
            buffer.write("It also dropped a key!\n")
            i.append("Key")
        os.system('cls')
        printcombat(buffer,open("battlewin.txt", "r"))
        open("combatbuffer.txt", 'w').close()
        input()
        list_to_pickle(inventory_file, i)
        stats = [hp, gp]
        list_to_pickle(stats_file, stats)
        return 1        
    if hp <= 0:
        buffer.write("You have fallen to the monster.\n")
        os.system('cls')
        printcombat(buffer,open("battlelose.txt", "r"))
        open("combatbuffer.txt", 'w').close()
        input()
        list_to_pickle(inventory_file, i)
        stats = [hp, gp]
        list_to_pickle(stats_file, stats)        
        return 0
        
def key_drop(i, door_state):
#############################################################################
#   Programmer Name: Peyton Davis					    #	    
#   Date: 12/12/16							    #
#   Purpose: A chance to drop a key after beating a monster                 #
#   Input: The player's inventory and the state of the door                 #
#   Output: A state to cause a drop or not cuase a drop                     #
#############################################################################
    """A chance to drop a key after beating a monster"""
    CHANCE = [0,1,2]
    RNG = random.choice(CHANCE)
    if RNG == 1:
        if door_state == 0:
            return 1
    else:
        return 0
                
def armor_rating(inv):
#############################################################################
#   Programmer Name: Alec Perry                                             #
#   Date: 12-11/16                                                          #
#   Purpose: To check the armor in the inventory and return an armor rating #
#   Input: inv                                                              #
#   Output: armor rating number                                             #
#############################################################################
    if "Leather" in inv:
        return 1
    elif "Chain Mail" in inv:
        return 2
    elif "Steel Plate" in inv:
        return 3
    else:
        return 0


def sword_rating(inv):
#############################################################################
#   Programmer Name: Alec Perry                                             #
#   Date: 12-13/16                                                          #
#   Purpose: To check the sword in the inventory and return an sword rating #
#   Input: inv                                                              #
#   Output: sword rating number                                             #
#############################################################################
    if "Wooden" in inv:
        return random.randint(3,6)
    elif "Iron" in inv:
        return random.randint(4,7)
    elif "Steel" in inv:
        return random.randint(5,8)
    else:
        return random.randint(1,3)



def printcombat(text,picture):    
#############################################################################
#   Programmer Name: Alec Perry                                             #             
#   Date: 12-13/16                                                          # 
#   Purpose: To display a graphical depiction of combat within a frame      #
#   Input: text, picture                                                    #
#   Output: framed graphical depiction of combat                            #
#############################################################################   
    width=77
    height=12
    height1=4
    p={}
    r={}
    s={}
    pp={}
    rr={}
    ss={}
    rowspace = "|"+str(width*" "+"|")
    rowunderscore = "|"+str(width*"_"+"|")
    for x in range(1,height+1):
        r["rd{}".format(x)]=text.readline()
    for y in range(1,height+1):
        s["sp{}".format(y)]=width-len(r["rd{}".format(y)])-2
    for a in range(1,height1):
        rr["rdd{}".format(a)]=picture.readline()
    for b in range(1,height1):
        ss["spp{}".format(b)]=width-len(rr["rdd{}".format(b)])-2
    
    print(" "+str(width*"_"))    
    print(rowspace)
    for c in range(1,height1):
        if rr["rdd{}".format(c)] == "":
            print(rowspace)
        else:
            pp["prr{}".format(c)]=print("|",rr["rdd{}".format(c)][:-1],ss["spp{}".format(c)]*" ","|")
    print(rowunderscore)    
    print(rowspace)
    for z in range(1,height+1):
        if r["rd{}".format(z)] == "":
            print("|"+str(width*" "+"|"))
        else:
            p["pr{}".format(z)]=print("|",r["rd{}".format(z)][:-1],s["sp{}".format(z)]*" ","|")
    print(rowunderscore)
    print(rowspace)
    print("|  "+"1 - Attack  | 2 - Use Potions | 'i' - Open inventory | 'Enter' - Continue  "+"|")
    print(rowunderscore)

def printinventory(i, gp):
#############################################################################
#   Programmer Name: Alec Perry                                             #
#   Date: 12-14/16                                                          #
#   Purpose: To display the player’s inventory within a frame               #
#   Input: i, gp	                                                    #
#   Output: framed display of the player’s inventory                        #
#############################################################################
    width=77
    height=25

    rowspace = "|"+str(width*" "+"|")
    rowunderscore = "|"+str(width*"_"+"|")
    print(" "+str(width*"_"))    
    print(rowspace)
    print("| "+"INVENTORY:"+(width-11)*" "+"|")
    print(rowspace)
    print("| "+"Gold:",gp,(width-8-len(str(gp)))*" "+"|")
    print(rowspace)
    for sword in i:
        if sword == "Stick" or sword == "Wooden" or sword == "Iron" or sword == "Steel":
            print("| Sword:"+(width-7)*" "+"|")
            print("| "+str(sword)+(width-len(sword)-1)*" "+"|")
            print(rowspace)
    for armor in i:
        if armor == "Tunic" or armor == "Leather" or armor == "Chain Mail" or armor == "Steel Plate":
            print("| Armor:"+(width-7)*" "+"|")
            print("| "+str(armor)+(width-len(armor)-1)*" "+"|")
            print(rowspace)
    pots = {"Healing": 0,"Strength": 0 ,"Defense": 0}
    pot = ["Healing","Strength","Defense"]
    space = 0
    for potion in i:
        if potion in pot:
            pots[potion]+= 1
    if pots["Healing"] > 0 or pots["Strength"] > 0 or pots["Defense"] > 0:
        print("| Potions:"+(width-9)*" "+"|")
        if pots["Healing"] > 0:
            print("| Healing Potion x"+str(pots["Healing"])+(width-18)*" "+"|")
        else:
            space+= 1
        if pots["Strength"] > 0:
            print("| Strength Potion x"+str(pots["Strength"])+(width-19)*" "+"|")
        else:
            space+= 1
        if pots["Defense"] > 0:
            print("| Defense Potion x"+str(pots["Defense"])+(width-18)*" "+"|")
        else:
            space+= 1
    for x in range(0,space+(height-15)):
        print(rowspace)
    print(rowunderscore)

########################################################

# PRINTMOVE

def printmove(the_file, health, inventory, direction, floor, complete):    
    ### builds then prints each 'frame' ###
    room = open_file(the_file, "r")
    width=77
    height=15
    p={}
    r={}
    s={}
    rowspace = "|"+str(width*" "+"|")
    rowunderscore = "|"+str(width*"_")+"|" 
    for x in range(1,height+1):
        r["rd{}".format(x)]=room.readline()
    for y in range(1,height+1):
        s["sp{}".format(y)]=width-len(r["rd{}".format(y)])-2
    
    print(" "+str(width*"_"))    
    print(rowspace)
    for z in range(1,height+1):
        if r["rd{}".format(z)] == "":
            print("|"+(width)*" "+"|")
        else:
            p["pr{}".format(z)]=print("|     ",r["rd{}".format(z)][:-1],(s["sp{}".format(z)]-5)*" ","|")
    print("|"+"___________ "+(width-12)*"_"+"|")
    
    # sword + armor stuff
    swords = ["Stick","Wooden","Iron","Steel"]
    for item in inventory:
        if item in swords:
            sword = item
    armors = ["Tunic","Leather","Chain Mail","Steel Plate"]
    for item in inventory:
        if item in armors:
            armor = item    
    # floor stuff
    floornum = floor
    # key stuff
    if complete == 1:
        statement = " - You found the key! To the door!"
    else:
        statement = " - Look for the key to unlock the way through!"
    # direction stuff
    up,down,left,right = "W","S","A "," D"
    if direction == "w":
        up="|"
    elif direction == "s":
        down="|"
    elif direction == "d":
        right=" -"
    elif direction == "a":
        left="- "
    print("| DIRECTION |"+(width-12)*" "+"|")
    print("|           |"+"  FLOOR: "+str(floornum)+\
          "   HEALTH: "+str(int(health))+"/20   SWORD: "+sword+"   ARMOR: "+ \
          armor+(width-len(sword)-len(armor)-len(str(int(health)))-56)*" "+"|")
    print("|     "+str(up)+"     |"+(width-12)*"_"+"|")
    print("|   "+str(left)+"@"+str(right)+"   |"+(width-12)*" "+"|")
    print("|     "+str(down)+"     |"+statement+(width-12-len(statement))*" "+"|")
    print("|___________|"+(width-12)*"_"+"|")

#########################################

#SHOP
    
def shop(inventory_file, stats_file):
#############################################################################
#   Programmer Name: Jared Janak, Alec Perry                                #
#   Date: 12-14/16                                                          #
#   Purpose: To allow the player to purchase items with their gold          #
#   Input: gp, inv                                                          #
#   Output: gp, inv                                                         #
#############################################################################
    inv = pickle_to_list(inventory_file)
    stats = pickle_to_list(stats_file)
    gp = stats[1]
    ### the shop that the player can see between levels. ###
    count= 0
    potion= {"Healing ": 50, "Strength ": 125, "Defense ": 150}
    sword= {"Wooden ": 75, "Iron ": 250, "Steel ": 500}
    armor= {"Leather ": 75, "Chain Mail ": 250, "Steel Plate ": 500}
    potions= ["Healing ","Strength ","Defense "]
    swords= ["Wooden ","Iron ","Steel ","Stick "]
    armors= ["Leather ","Chain Mail ","Steel Plate ","Tunic "]
    submenu= [potion, sword, armor]
    submenus= [potions, swords, armors]
    names= ["Potion", "Sword", "Armor"]
    buffer= open("shopbuffer.txt", "r+")

    buffer.write("Welcome to the shop.\n\n")    
    while count!= 1:
        buffer.write("i - View Inventory\n1 - Potions\n2 - Weapons\n"+\
                     "3 - Armor\n4 - Exit Shop\n\nYou have "+\
                     str(gp)+" gold.\n")
        os.system('cls')
        printshop(buffer, open("shoppic.txt", "r"))
        choice= input("")
        open("shopbuffer.txt", 'w').close()
        
        if choice== "i":
            os.system('cls')
            printinventory(inv, gp)
            input("")
            continue                
        elif choice== "1" or choice== "2" or choice== "3":
            if choice== "1":
                c1= 0
                buffer.write("1 - Healing Potion - 50 gold\n"+\
                             "    ~ Effect: Heals 10 HP\n\n"+\
                             "2 - Strength Potion - 125 gold\n"+\
                             "    ~ Effect: Next 3 turns do 1.5x damage\n\n"+\
                             "3 - Defense Potion - 150 gold\n"+\
                             "    ~ Effect: Next 3 turns take .5x damage\n\n" +\
                             "4 - Back\n\n")
                
            if choice== "2":
                c1= 1
                buffer.write("1 - Wooden Sword - 75 gold\n"+\
                             "    ~ Attack: 3-6 damage\n\n"+\
                             "2 - Iron Sword - 250 gold\n"+\
                             "    ~ Attack: 4-7 damage\n\n"+\
                             "3 - Steel Sword - 500 gold\n"+\
                             "    ~ Attack: 5-8 damage\n\n" +\
                             "4 - Back\n\n")
                
            elif choice== "3":
                c1= 2
                buffer.write("1 - Leather Armor - price: 75 gold\n"+\
                             "    ~ Enemy Attack: -1\n\n"+\
                             "2 - Chain Mail - Price: 250 gold\n"+\
                             "    ~ Enemy Attack: -2\n\n"+\
                             "3 - Steel Plate Armor - Price: 500 gold\n"+\
                             "    ~ Enemy Attack: -3\n\n" +\
                             "4 - Back\n\n")
                            
            buffer.write("What would you like to buy?\n")
            os.system('cls')
            printshop(buffer, open("shoppic.txt", "r"))
            open("shopbuffer.txt", 'w').close()
            try:
                c2= int(input(""))
            except:
                continue
            if c2 == 4:
                continue
            buffer.write("Do you want to buy a "+str(submenus[c1][c2-1])+\
                         names[c1]+" for "+str(submenu[c1][submenus[c1][c2-1]])+\
                         " gold?\n1 - Yes\n2 - No\n")
            os.system('cls')
            printshop(buffer, open("shoppic.txt", "r"))
            open("shopbuffer.txt", 'w').close()
            choice2= int(input(""))
            if choice2== 1:
                if gp>= submenu[c1][submenus[c1][c2-1]]:
                    gp-= submenu[c1][submenus[c1][c2-1]]
                    if c1== 1 or c1== 2:
                        for i in range(0,4):
                            den= (submenus[c1][i])[:-1]
                            if den in inv:
                                inv.remove(den)                   
                    inv.append(str(submenus[c1][c2-1])[:-1])
                else:
                    buffer.write("You don't have enough gold to buy that.\n")
                    os.system('cls')
                    printshop(buffer, open("shoppic.txt", "r"))
                    input("")
            if choice== 2:
                continue                                                    
        elif choice== "4":
            count+= 1
            open("shopbuffer.txt", 'w').close()
            buffer.write("You leave the shop.\n")
            os.system('cls')
            printshop(buffer, open("shoppic.txt", "r"))
            input("")
            open("shopbuffer.txt", 'w').close()
            list_to_pickle(inventory_file, inv)
            stats[1] = gp
            list_to_pickle(stats_file, stats)

def printshop(text,picture):    
#############################################################################
#   Programmer Name: Alec Perry                                             #
#   Date: 12-15/16                                                          #
#   Purpose: To display the shop within a frame                             #
#   Input: text, picture                                                    #
#   Output: framed shop display                                             #
#############################################################################
    width=77
    height=12
    heightpic=7
    p={}
    r={}
    s={}
    pp={}
    rr={}
    ss={}
    rowspace = "|"+str(width*" "+"|")
    rowunderscore = "|"+str(width*"_"+"|")
    for x in range(1,height+1):
        r["rd{}".format(x)]=text.readline()
    for y in range(1,height+1):
        s["sp{}".format(y)]=width-len(r["rd{}".format(y)])-2
    for a in range(1,heightpic+1):
        rr["rdd{}".format(a)]=picture.readline()
    for b in range(1,heightpic+1):
        ss["spp{}".format(b)]=width-len(rr["rdd{}".format(b)])-2
    
    print(" "+str(width*"_"))    
    print(rowspace)
    for c in range(1,heightpic+1):
        if rr["rdd{}".format(c)] == "":
            print(rowspace)
        else:
            pp["prr{}".format(c)]=print("|",rr["rdd{}".format(c)][:-1],ss["spp{}".format(c)]*" ","|")
    print(rowunderscore)    
    print(rowspace)
    for z in range(1,height+1):
        if r["rd{}".format(z)] == "":
            print("|"+str(width*" "+"|"))
        else:
            p["pr{}".format(z)]=print("|",r["rd{}".format(z)][:-1],s["sp{}".format(z)]*" ","|")
    print(rowunderscore)

def printinventory(i, gp):
#############################################################################
#   Programmer Name: Alec Perry                                             #
#   Date: 12-14/16                                                          #
#   Purpose: To display the player’s inventory within a frame               #
#   Input: i, gp	                                                    #
#   Output: framed display of the player’s inventory                        #
#############################################################################
    width=80
    height=20

    rowspace = "|"+str(width*" "+"|")
    rowunderscore = "|"+str(width*"_"+"|")
    print(" "+str(width*"_"))    
    print(rowspace)
    print("| "+"INVENTORY:"+(width-11)*" "+"|")
    print(rowspace)
    print("| "+"Gold:",gp,(width-8-len(str(gp)))*" "+"|")
    print(rowspace)
    for sword in i:
        if sword == "Stick" or sword == "Wooden" or sword == "Iron" or sword == "Steel":
            print("| Sword:"+(width-7)*" "+"|")
            print("| "+str(sword)+(width-len(sword)-1)*" "+"|")
            print(rowspace)
    for armor in i:
        if armor == "Tunic" or armor == "Leather" or armor == "Chain Mail" or armor == "Steel Plate":
            print("| Armor:"+(width-7)*" "+"|")
            print("| "+str(armor)+(width-len(armor)-1)*" "+"|")
            print(rowspace)
    pots = {"Healing": 0,"Strength": 0 ,"Defense": 0}
    pot = ["Healing","Strength","Defense"]
    space = 0
    for potion in i:
        if potion in pot:
            pots[potion]+= 1
    if pots["Healing"] > 0 or pots["Strength"] > 0 or pots["Defense"] > 0:
        print("| Potions:"+(width-9)*" "+"|")
        if pots["Healing"] > 0:
            print("| Healing Potion x"+str(pots["Healing"])+(width-18)*" "+"|")
        else:
            space+= 1
        if pots["Strength"] > 0:
            print("| Strength Potion x"+str(pots["Strength"])+(width-19)*" "+"|")
        else:
            space+= 1
        if pots["Defense"] > 0:
            print("| Defense Potion x"+str(pots["Defense"])+(width-18)*" "+"|")
        else:
            space+= 1
    for i in range(0,space+(height-15)):
        print(rowspace)
    print(rowunderscore)
    
########################################################

# MAIN FUNCTION

def main():
#############################################################################
#   Programmer Name: Peyton Davis					    #	    
#   Date: 12/12/16							    #
#   Purpose: Everything needed to run the game                              #
#   Input: NA                                                               #
#   Output: NA                                                              #
#############################################################################
    """Everything needed to run the game"""
    level = 1
    start(4)
    os.system("color 07")
    while 1 == 1:
        os.system('cls')
        switch_map("maps.txt")
        add_monsters("current_map.txt", "monster_stats.txt")
        move("current_map.txt", "inventory.txt", "stats.txt", "monster_stats.txt", level)
        shop("inventory.txt", "stats.txt")
        level += 1
        update_difficulty("monster_stats.txt")
        
    input("\n\nPress the enter key to exit")

#########################################################

# FONT

def setfont():
#############################################################################
#   Programmer Name: Alec Perry 					    #	    
#   Date: 12/12/16							    #
#   Purpose: sets the correct font and size                                 #
#   Input: NA                                                               #
#   Output: NA                                                              #
#############################################################################
    LF_FACESIZE = 32
    STD_OUTPUT_HANDLE = -11

    class COORD(ctypes.Structure):
        _fields_ = [("X", ctypes.c_short), ("Y", ctypes.c_short)]

    class CONSOLE_FONT_INFOEX(ctypes.Structure):
        _fields_ = [("cbSize", ctypes.c_ulong),
                    ("nFont", ctypes.c_ulong),
                    ("dwFontSize", COORD),
                    ("FontFamily", ctypes.c_uint),
                    ("FontWeight", ctypes.c_uint),
                    ("FaceName", ctypes.c_wchar * LF_FACESIZE)]

    font = CONSOLE_FONT_INFOEX()
    font.cbSize = ctypes.sizeof(CONSOLE_FONT_INFOEX)
    font.nFont = 48
    font.dwFontSize.X = 14
    font.dwFontSize.Y = 21
    font.FontFamily = 54
    font.FontWeight = 400
    font.FaceName = "Consolas"

    handle = ctypes.windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)
    ctypes.windll.kernel32.SetCurrentConsoleFontEx(
            handle, ctypes.c_long(False), ctypes.pointer(font))

#########################################################

# MAIN

# Imports
import pickle
import random
import sys
import os
import ctypes

# Start Inventory and Monster Data
inventory = ["Healing","Stick","Tunic"]
list_to_pickle("inventory.txt", inventory)
health_and_gold = [20, 0]
list_to_pickle("stats.txt", health_and_gold)
monster_stats = [[3,4,5,6], [0,1,2], [5,6,7,8], [0]]
list_to_pickle("monster_stats.txt", monster_stats)

# Clearing Screen
clear = lambda: os.system('cls')

# Name Application
os.system("title Dungeon Dweller")

# Setting Window
os.system('mode con: cols=85 lines=26')
setfont()

# Main
main()
input()
