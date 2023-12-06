file = open('input_04.txt', 'r')
scratchcards = [line.split(':')[1] for line in file.readlines()]
file.close()

ans = 0
for i in range(len(scratchcards)):
  wins, have = scratchcards[i].split('|')
  wins, have = wins.split(), have.split()
  if not any([num in have for num in wins]):
    ans += 0
  else:
    ans += 2**( sum( [num in have for num in wins] ) - 1)
print(ans)
