import itertools

def fin(current_game):
	def all_same(l):
		if l.count(l[0]) == len(l) and l[0] != 0:
			return True
		else:
			return False

 	# horizontal
	for row in game:
		print(row)
		if all_same(row):
			print(f"player {row[0]} is the winner horizontally!")
			return True

	# diagonal
	diags = []
	for col, row in enumerate(reversed(range(len(game)))):
		diags.append(game[row][col])
	if all_same(diags):
		print(f"player {diags[0]} is the winner diagonally (/)!")
		return True

	diags = []
	for ix in range(len(game)):
		diags.append(game[ix][ix])
	if all_same(diags):
		print(f"player {diags[0]} is the winner diagonally (\\)!")
		return True

	# vertical
	for col in range(len(game)):
		check = []

		for row in game:
			check.append(row[col])

		if all_same(check):
			print(f"Player {check[0]} is the winner vertically (|)!")
			return True
	# Tie
	for row in current_game:
		for col in row:
			if col == 0:
				return False
	print("Stalemate! It's a tie.")
	return True

def game_board(game_map, player=0, row=0, column=0, just_display=False):
	try:
		if game_map[row][column] != 0:
			print("this position is occupado! choose another!")
			return game_map, False
		print("   "+"  ".join([str(i) for i in range(len(game_map))]))
		if not just_display:
			game_map[row][column] = player
		for count, row in enumerate(game_map):
			print(count, row)
		return game_map, True

	except IndexError as e:
		print("select row/column as 0 1 or 2", e)
		return game_map, False
		
	except Exception as e:
		print("something went wrong", e)
		return game_map, False

play = True
players = [1, 2]
while play:
	game = [[0 for i in range(3)] for i in range(3)]
	game_won = False
	game, _ = game_board(game, just_display=True)
	player_choice = itertools.cycle([1, 2])
	while not game_won:
		current_player = next(player_choice)
		print(f"Current Player: {current_player}")
		played = False
		while not played:
			column_choice = int(input("what column do you want to play? (0, 1, 2): "))
			row_choice = int(input("what row do you want to play? (0, 1, 2): "))
			game, played = game_board(game, current_player, row_choice, column_choice)

		if fin(game):
			game_won = True
			again = input("The game is over, would you like to play again? y/n) ")
			if again.lower() == "y":
				print("restarting game")
			elif again.lower() == "n":
				print("Thanks for play, bye")
				play = False
			else:
				print("Thanks for play, bye")
				play = False
