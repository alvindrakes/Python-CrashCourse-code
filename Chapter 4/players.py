# slicing a list 

players = ['alvin', 'kon', 'chan', 'shawn', 'nigga']
print(players[0:3]) # print 1st 3 elements in the list 

print(players[1:4])  # print from 2nd to 5th elements

print(players[:4]) # if we omit the 1st index, python automatically starts at the beginnig 

print(players[2:]) # same thing, but print from 3rd element to the last 

print(players[-3:]) # print last 3 players 

print(players[:-3])

print('\nHere is the first 3 players in my team!')
for player in players[:3]:
	print(player.title())