with open('Day4input.txt') as rawInput:
    input = rawInput.readlines()
    data = []
    for i in input:
        data.append(i.strip('\n'))

results = data.pop(0)
squares = []
interimList = []
data.pop(0)

for i in data:
    if i == '':
        squares.append(interimList)
        interimList = []
    else:
        interimList.append(i.split(' '))

results = results.split(',')
for i in results:
    winner = False
    for x in range(len(squares)):
        for y in range(len(squares[x])):
            for j in range(len(squares[x][y])):
                continue
    if winner == True:
        continue
print('X' in squares[0][0][0])
squares[0][0][0] = squares[0][0][0] + 'X'
print(squares[0][0][0])
print('37' in squares[0][0][0])