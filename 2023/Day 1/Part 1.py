file = open('input_01.txt', 'r')
data = file.readlines()
file.close()

values = [0] * len(data)
for i in range(len(data)):
  num = [n for n in data[i] if n.isdigit()]
  values[i] = int(str(num[0]) + str(num[-1]))

print(sum(values))