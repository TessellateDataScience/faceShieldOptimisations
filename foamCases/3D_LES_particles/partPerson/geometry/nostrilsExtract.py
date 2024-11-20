# initiation
with open('person.stl') as f:
    lines = f.readlines()
target1 = '  facet normal 0 0 -1\n'
target2 = '  facet normal -0 0 -1\n'
check = ' 20\n'
lineNumber = 0

with open('nostrils.stl', 'w') as f2:
    f2.write('solid nostrils\n')
with open('personNoNostrils.stl', 'w') as f3:
    print('starting...')

# write data to files
while lineNumber < len(lines):
    line = lines[lineNumber]
    #print(lineNumber)
    if line == target1 or line == target2:
        lineCheck = lines[lineNumber + 2]
        lineCheck = lineCheck[-4:]
        if lineCheck == check:
            with open('nostrils.stl', 'a') as f2: 
                for lineNumbers in range(7):
                    f2.write(lines[lineNumber + lineNumbers])
            lineNumber = lineNumber + 7
        else:
            with open('personNoNostrils.stl', 'a') as f3:
                for lineNumbers in range(7):
                    f3.write(lines[lineNumber + lineNumbers])           
            lineNumber = lineNumber + 7           
    else:
        with open('personNoNostrils.stl', 'a') as f3:
            f3.write(line)           
        lineNumber = lineNumber + 1
with open('nostrils.stl', 'a') as f2:
    f2.write('endsolid nostrils')
print('...completed.')