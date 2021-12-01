count = 0
with open('inputs.txt') as f:
    previous = int(next(f))
    for line in f:
        number = int(line.strip())
        if previous < number: count += 1
        previous = number
     
print(count)
