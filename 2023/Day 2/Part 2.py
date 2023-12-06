file = open('input_02.txt', 'r')
games = [line.strip().split(':')[1] for line in file.readlines()]
file.close()

power = [0]*len(games)
for i, game in enumerate(games):
  cubes = {"red": 0, "green": 0, "blue": 0}
  for draw in game.split(';'):
    for cube in draw.split(','):
      n, colour = cube.split()
      cubes[colour] = max(cubes[colour], int(n))
  power[i] = cubes['red'] * cubes['green'] * cubes['blue']

print(sum(power))
