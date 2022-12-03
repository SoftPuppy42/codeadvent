def score(player1, player2):
	if (player1 - 1) % 3 == player2:
		return player2 + 1
	elif (player2 - 1) % 3 == player1:
		return player2 + 7
	return player2 + 4

with open("input.txt", "r") as f:
	data = f.read().splitlines()
	data = [line.split() for line in data]
	data = [(ord(player1) - ord("A"), ord(player2) - ord("X")) for player1, player2 in data]

roundend = [(player1, (player1 + player2 - 1) % 3) for player1, player2 in data]

print(sum(score(player1, player2) for player1, player2 in data))
print(sum(score(player1, player2) for player1, player2 in roundend))