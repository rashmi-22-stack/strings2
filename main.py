# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line
#part 1.
player_1 = 'Ruud Gullit'
player_2 = 'Marco van Basten'

goal_0 = 32
goal_1 = 54

scorers = player_1 +' ' + str(goal_0) + ',' + ' ' +  player_2 + " "+ str(goal_1)
print(scorers)

report = f'{player_1} scored in the  {goal_0}nd minute\n{player_2} scored in the {goal_1}th minute.'
print(report)
# part2.
player = "Ruud Gullit"
first_name = player[:player.find(" ")]
print(first_name)

last_name = player[player.find(" ")+1:]
print(last_name)

last_name_len = len(last_name)
print(last_name_len)
#name_short = player[0]+"."+" "+ player[-6:] or
name_short = first_name[0]+ "."+" "+last_name
print(name_short)

chant = (first_name + '! ')*len(first_name)
print(chant)
good_chant = chant[:-1] != " "
print(good_chant)


