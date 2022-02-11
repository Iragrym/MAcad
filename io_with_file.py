from pprint import pprint

t = int(input())

data = []
for _ in range(t):
    n = input()
    line = input()
    words = line.split()
    data.append(words)
    
print('Считанные данные')
pprint(data)