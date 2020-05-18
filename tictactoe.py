import itertools

def game_board(game_map, player=0, row=0, column=0, just_display= False):
	try:
		if game_map[row][column] != 0:
			print("already occupied choose another!!")
			return game_map, False
		print("   0  1  2")
		if not just_display:
			game_map[row][column] = player
		for count, row in enumerate(game_map):
			print(count, row)
		return game_map, True
	
	except IndexError as e:
		print("something went wrong ",e)
		return game_map, False
	
	except Exception as e:
		print("something went very wrong!!",e)
		return game_map, False

def win(current_game):
	#horizontal
	for row in game:
		print(row)
		if row.count(row[0]) == len(row) and row[0] != 0:
			print(f"player {row[0]} is winner horizontally!!!")
			return True
	#vertical
	for col in range(len(game)):
		check = []
		for row in game:
			check.append(row[col])

		if check.count(check[0]) == len(check) and check[0] != 0 :
			print(f"player {check[0]} is winner vertically!!!")
			return True	
	#diagonal	
	diags = []
	for ix in range(len(game)):
		diags.append(game[ix][ix])
	if diags.count(diags[0]) == len(diags) and diags[0] != 0 :
		print(f"player {diags[0]} is winner diagonally(\\)!!!")
		return True
	diags = []
	for col, row in enumerate(reversed(range(len(game)))):
		diags.append(game[row][col])
	if diags.count(diags[0]) == len(diags) and diags[0] != 0 :
		print(f"player {diags[0]} is winner diagonally(/)!!!")
		return True

	return False				

play = True
players = [1, 2]
while play:
	game = [[0, 0, 0],
	        [0, 0, 0],
	        [0, 0, 0]]

	game_won = False
	game, played = game_board(game, just_display=True)
	player_choice = itertools.cycle([1, 2])
	while not game_won:
		current_player = next(player_choice)
		print(f"current_player :  {current_player}")
		played = False

		while not played:
			row_choice = int(input("what row do you want to play?  (0, 1, 2):  "))
			column_choice = int(input("what column do you want to play?  (0, 1, 2):  "))
			game, played = game_board(game, current_player, row_choice, column_choice)

		if win(game):
			game_won = True
			again = input("The game is over, would you like to play again? (y/n) :  ")	
			if again.lower() == "y":
				print("restarting!!")
			elif again.lower() == "n":
				print("bye!!")
				play = False
			else:
				print("Not a valid option")
				play = False
