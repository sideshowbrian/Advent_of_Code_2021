data = []
with open('Inputs.txt') as f:
    for line in f:
        number = int(line.strip())
        # print(number)
        data.append(number)

prevous = data[0]+data[1]+data[2]

count = 0
for i in range(1, len(data)-1):
    window = data[i-1]+data[i]+data[i+1]
    print(i, window)
    if window > prevous: count +=1
    prevous = window

print(count)
