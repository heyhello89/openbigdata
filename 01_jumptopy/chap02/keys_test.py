# coding: cp949
player={"Yeona Kim":"Figure skating","Hyunjin Ryu":"Baseball","Jisung Park":"Soccer"}
print("Step1] Printing the raw type of dictionaty,'player'")
print(player)

print("\nStep2] Printing the key lists using player.keys() function")
print(player.keys())

print("\nStep3] Printing the values lists using player.values() function")
print(player.values())

print("\nStep4] Trying to search character of 'Hyunjin Ryu' in the player dictionary")
for player_key in player.keys():
	print(player_key)
	if player_key == 'Hyunjin Ryu':
            print("\nI found Hyunjin Ryu! Now, I will tell you about him.")
            print("He is a "+player['Hyunjin Ryu']+" player 한글")
#                print("He is a "+player['Hyunjin Ryu']+" player")
            break

print("\nProgram End")
