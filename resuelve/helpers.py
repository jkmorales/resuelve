levels = {'A' : 5,'B' : 10,'C' : 15,'Cuauh' : 20}

def get_percent_individual(goals:int, level:str):
	return goals / levels[level] if goals < levels[level] else 1

def get_percent_grupal(data:dict):
	goals_per_month = 0
	minimum_required = 0
	for player in data:
		goals_per_month += player['goles']
		minimum_required += levels[player['nivel']]
	return goals_per_month / minimum_required if goals_per_month < minimum_required else 1