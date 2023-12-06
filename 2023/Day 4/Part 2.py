file = open('input_04.txt', 'r')
scratchcards = [line.split(':')[1] for line in file.readlines()]
file.close()

copies = [1]*len(scratchcards)
for i, card in enumerate(scratchcards):
  wins, have = map(str.split, card.split('|'))
  matches = sum([num in have for num in wins])
  if matches > 0:
    for j in range(matches):
      copies[i+1+j] += copies[i]

print( sum(copies) )
