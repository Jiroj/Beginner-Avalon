import osimport randomimport shutilimport sysdef main():        players = ["Bacon", "Choki", "Ferlyn", "Geo", "Hish", "Kappy", "Karina", "Montana", "Nobie", "Shu"]        if not (len(players) is 10):                print("Invalid number of players")                exit(1)                        num_players = len(players)        players = set(players) # use as set to avoid duplicate players        players = list(players) # convert to list        random.shuffle(players) # ensure random order, though set should already do that        if len(players) != num_players:                print("No duplicate player names")                exit(1)        all_good_roles_in_order = ["Percival", "Merlin", "Vanilla1", "Vanilla2", "Vanilla3", "Vanilla4"]        all_evil_roles_in_order = ["Mordred", "Assassin", "Oberon", "Morgana"]        # assign the roles in the game        good_roles = ["Percival", "Merlin", "Vanilla1", "Vanilla2", "Vanilla3", "Vanilla4"]        evil_roles = ["Mordred", "Assassin", "Oberon", "Morgana"]        # shuffle the roles        random.shuffle(good_roles)        random.shuffle(evil_roles)        # determine the number of roles in the game        if num_players == 10:                num_evil = 4                num_good = 6        # assign players to teams        assignments = {}        reverse_assignments = {}        good_roles_in_game = set()        evil_roles_in_game = set()        good_players = players[:num_good]        evil_players = players[num_good:num_good + num_evil]        # assign good roles        for good_player in good_players:                player_role = good_roles.pop()                assignments[good_player] = player_role                reverse_assignments[player_role] = good_player                good_roles_in_game.add(player_role)        # assign evil roles        for evil_player in evil_players:                player_role = evil_roles.pop()                assignments[evil_player] = player_role                reverse_assignments[player_role] = evil_player                evil_roles_in_game.add(player_role)        # delete and recreate game directory        if os.path.isdir("game"):                shutil.rmtree("game")        os.mkdir("game")        # make every role's file        # Merlin sees: Morgana, Maleagant, Oberon, Agravaine, Colgrevance, Lancelot* as evil        if "Merlin" in good_roles_in_game:                # determine who Merlin sees                seen = []                for evil_player in evil_players:                        if assignments[evil_player] != "Mordred":                                seen.append(evil_player)                                                random.shuffle(seen)                                # and write this info to Merlin's file                player_name = reverse_assignments["Merlin"]                filename = "game/" + player_name + ".txt"                with open(filename, "w") as file:                        file.write("You are Merlin.\n")                        file.write("You know the agents of Evil, but you must speak of this only in riddle. If your true identity is discovered, all will be lost.\n\n")                        for seen_player in seen:                                file.write("You see " + seen_player + " as evil.\n")        # Percival sees Merlin, Morgana* as Merlin        if "Percival" in good_roles_in_game:                # determine who Percival sees                seen = []                if "Merlin" in good_roles_in_game:                        seen.append(reverse_assignments["Merlin"])                if "Morgana" in evil_roles_in_game:                        seen.append(reverse_assignments["Morgana"])                random.shuffle(seen)                                # and write this info to Percival's file                player_name = reverse_assignments["Percival"]                filename = "game/" + player_name + ".txt"                with open(filename, "w") as file:                        file.write("You are Percival.\n")                        for seen_player in seen:                                file.write("You see " + seen_player + " as Merlin (or Morgana).\n")        # Vanilla 1        if "Vanilla1" in good_roles_in_game:                player_name = reverse_assignments["Vanilla1"]                filename = "game/" + player_name + ".txt"                with open(filename, "w") as file:                        file.write("You are a Loyal Servant of Arthur, on the side of Good.\n")        # Vanilla 2        if "Vanilla2" in good_roles_in_game:                player_name = reverse_assignments["Vanilla2"]                filename = "game/" + player_name + ".txt"                with open(filename, "w") as file:                        file.write("You are a Loyal Servant of Arthur, on the side of Good.\n")        # Vanilla 3        if "Vanilla3" in good_roles_in_game:                player_name = reverse_assignments["Vanilla3"]                filename = "game/" + player_name + ".txt"                with open(filename, "w") as file:                        file.write("You are a Loyal Servant of Arthur, on the side of Good.\n")        # Vanilla 4        if "Vanilla4" in good_roles_in_game:                player_name = reverse_assignments["Vanilla4"]                filename = "game/" + player_name + ".txt"                with open(filename, "w") as file:                        file.write("You are a Loyal Servant of Arthur, on the side of Good.\n")                # make list of evil players seen to other evil        evil_players_no_oberon = list(set(evil_players))        if "Oberon" in evil_roles_in_game:                evil_players_no_oberon = list(set(evil_players_no_oberon) - set([reverse_assignments["Oberon"]]))                        random.shuffle(evil_players_no_oberon)        if "Mordred" in evil_roles_in_game:                player_name = reverse_assignments["Mordred"]                filename = "game/" + player_name + ".txt"                with open(filename, "w") as file:                        file.write("You are Mordred.\n")                        for evil_player in evil_players_no_oberon:                                if evil_player != player_name:                                        file.write(evil_player + " is a fellow member of the evil council.\n")                        if "Oberon" in evil_roles_in_game:                                file.write("There is an Oberon lurking in the shadows.\n")        if "Morgana" in evil_roles_in_game:                player_name = reverse_assignments["Morgana"]                filename = "game/" + player_name + ".txt"                with open(filename, "w") as file:                        file.write("You are Morgana.\n")                        for evil_player in evil_players_no_oberon:                                if evil_player != player_name:                                        file.write(evil_player + " is a fellow member of the evil council.\n")                                                if "Oberon" in evil_roles_in_game:                player_name = reverse_assignments["Oberon"]                filename = "game/" + player_name + ".txt"                with open(filename, "w") as file:                        file.write("You are Oberon.\n\n")                        file.write("You are Oberon, on the side of Evil.\n")                        file.write("You are not revealed to other Evil players, nor do you know which players are Evil at the start of the game.\n")                        #for evil_player in evil_players_no_oberon:#                                file.write(evil_player + " is a member of the evil council.\n\n")        if "Assassin" in evil_roles_in_game:                player_name = reverse_assignments["Assassin"]                filename = "game/" + player_name + ".txt"                with open(filename, "w") as file:                        file.write("You are the Assassin, on the side of Evil.\n")                        file.write("You have an additional evil objective: identify and assassinate Merlin at the end of the game.\n")                        for evil_player in evil_players_no_oberon:                                if evil_player != player_name:                                       file.write(evil_player + " is a fellow member of the evil council.\n")                # write start file        with open("game/start.txt", "w") as file:                file.write("The players proposing teams for the first mission are:\n")                team_lead = players                counter = 1                                for leader in players:                        file.write("[Mission {}] {} \n".format(counter, leader))                        counter += 1        # write do not open        with open("game/DoNotOpen.txt", "w") as file:                file.write("Player -> Role\n\nGOOD TEAM:\n")                for role in all_good_roles_in_order:                        if role in reverse_assignments:                                file.write(reverse_assignments[role] + " -> " + role + "\n")                file.write("\n\nEVIL TEAM:\n")                for role in all_evil_roles_in_order:                        if role in reverse_assignments:                                file.write(reverse_assignments[role] + " -> " + role + "\n")                file.write("\n\nMISCELLANEOUS:\n")                counter = 1                for leader in players:                        file.write("[Mission {}] {} \n".format(counter, leader))                        counter += 1if __name__ == "__main__":        main()