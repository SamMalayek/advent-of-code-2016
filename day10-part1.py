from collections import defaultdict
import math

def main():
	cmds = open('day10.txt', 'r').read().splitlines()
	bots = defaultdict(list)  # bot -> [lowVal, highVal]
	dag = defaultdict(list)  # bot -> lowBot, highBot

	def goNext(botNum):
		if len(bots[botNum]) == 2:
			bots[botNum].sort()
			lowBot = dag[botNum][0]
			hiBot = dag[botNum][1]
			lowBotVal = bots[botNum][0]
			hiBotVal = bots[botNum][1]
			if lowBotVal == 17 and hiBotVal == 61:
				print(botNum)
				quit()
			bots[lowBot].append(lowBotVal)
			bots[hiBot].append(hiBotVal)
			bots[botNum] = []
			goNext(lowBot)
			goNext(hiBot)

	# Create DAG and dict
	for cmd in cmds:
		parts = cmd.split(' ')
		if parts[0] == 'bot':
			botGiver = int(parts[1])
			# else is to separate Output bins from Bot bins
			lowBot = int(parts[6]) if parts[5] == 'bot' else ((int(parts[6])+13)*100)
			hiBot = int(parts[-1]) if parts[-2] == 'bot' else ((int(parts[-1])+13)*100)
			bots[botGiver] = []
			bots[lowBot] = []
			bots[hiBot] = []
			dag[botGiver] = [lowBot, hiBot]

	# Process values
	for cmd in cmds:
		parts = cmd.split(' ')
		if parts[0] == 'value':
			val = int(parts[1])
			botNum = int(parts[-1])
			bots[botNum].append(val)
			goNext(botNum)


if __name__ == "__main__":
	main()
