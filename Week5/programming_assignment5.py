def str_input():
	data_arr = []
	while True:
		s = input()
		if s == '':
			break
		else:
			s = s.split(':')
			s[2] = s[2].split(',')
			data_arr.append(s)
	for i in range(len(data_arr)):
		for j in range(len(data_arr[i][2])):
			data_arr[i][2][j] = data_arr[i][2][j].split('-')
	return(data_arr)

def top5(player,data):
	top5 = 0
	for i in data:
		if i[0] == player and len(i[2])>3:
			top5+=1
	return(top5)

def top3(player,data):
	top3 = 0
	for i in data:
		if i[0] == player and len(i[2])<=3:
			top3+=1
	return(top3)

def set_count(player,data):
	(sets_won, sets_lost) = (0, 0)
	for i in data:
		if player in i:
			if player == i[0]:
				for j in i[2]:
					if j[0]>j[1]:
						sets_won+=1
					else:
						sets_lost+=1
			if player == i[1]:
				for j in i[2]:
					if j[1]>j[0]:
						sets_won+=1
					else:
						sets_lost+=1
	return(sets_won,sets_lost)

def game_count(player,data):
	(games_won, games_lost) = (0, 0)
	for i in data:
		if player in i:
			if player == i[0]:
				for j in i[2]:
					games_won+=int(j[0])
					games_lost+=int(j[1])
			if player == i[1]:
				for j in i[2]:
					games_won+=int(j[1])
					games_lost+=int(j[0])
	return(games_won,games_lost)

def data_process(players,data):
	(temp, main) = ([], [])
	for i in players:
		temp = []
		temp.append(i)
		temp.append(top5(i,data))
		temp.append(top3(i,data))
		sets_won, sets_lost = set_count(i,data)
		games_won, games_lost = game_count(i,data)
		temp.append(sets_won)
		temp.append(games_won)
		temp.append(sets_lost)
		temp.append(games_lost)
		main.append(temp)
	return(main)

def data_sort(data):
	data = sorted(data, key=lambda x:x[1:4],reverse=True)
	return data


def main():
	data = str_input()
	players = list(set([j for i in data for j in i[0:2]]))
	processed_data = data_process(players, data)
	final_data=data_sort(processed_data)
	for i in final_data:
		print(" ".join(list(map(str,i))))

main()	
