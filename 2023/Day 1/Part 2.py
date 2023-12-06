file = open('input_01.txt', 'r')
data = file.readlines()
file.close()

values = [0] * len(data)
for i in range(len(data)):
  data[i] = data[i].replace("one", "o1e")
  data[i] = data[i].replace("two", "t2o")
  data[i] = data[i].replace("three", "t3e")
  data[i] = data[i].replace("four", "f4r")
  data[i] = data[i].replace("five", "f5e")
  data[i] = data[i].replace("six", "s6x")
  data[i] = data[i].replace("seven", "s7n")
  data[i] = data[i].replace("eight", "e8t")
  data[i] = data[i].replace("nine", "n9e")
  num = [n for n in data[i] if n.isdigit()]
  values[i] = int(str(num[0]) + str(num[-1]))

print(sum(values))
