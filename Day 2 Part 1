file = open('input_02.txt', 'r')
games = [line.strip().split(':')[1] for line in file.readlines()]
file.close()

cubes = {"red": 12, "green": 13, "blue": 14}

ans = 0
for i, game in enumerate(games):
  possible = True
  draws = game.split(';')
  for draw in draws:
    for cube in draw.split(','):
      n, colour = cube.split()
      if int(n) > cubes[colour]:
        possible = False
  if possible == True:
    ans += i+1

print(ans)
