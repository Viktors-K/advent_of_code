dir = r""

inputs = []

# opens file and reads it
with open(dir,'r') as f:
    for line in f:
        # removes newline char and adds to list
        inputs.append(line.removesuffix("\n"))

test = ['L68','L30','R48','L5','R60','L55','L1','L99','R14','L82']

# sets starting variables
position = 50
zeroes = 0
verbose = False

if verbose:
    print(f"The dial starts by pointing at {position}.")
for turn in inputs:
    if turn[0] == 'R':
        # if turning right, we add to position
        position += int(turn[1:])
        # if it goes out of bounds, we loop it back
        while (position > 99):
            position -= 100
    else:
        # if turning left, we subtract from position
        position -= int(turn[1:])
        # if it goes out of bounds, we loop it back
        while (position < 0):
            position += 100
    # after every turn, we check if we are at 0
    if position == 0:
        zeroes+=1
        if verbose:
            print(f"The dial is rotated {turn} to point at {position}!!!")
    else:
        if verbose:
            print(f"The dial is rotated {turn} to point at {position}.")

print(f"The safe code points at 0 a total of {zeroes} times. (part 1)")

# PART2

# resets starting variables
position = 50
zeroes = 0
verbose = True

if verbose:
    print(f"The dial starts by pointing at {position}.")
for action in test:
    turnedThroughZero = 0
    if action[0] == 'R':
        # if turning right, we add
        coefficient = 1
    else:
        # if turning left, we subtract
        coefficient = -1
    # vector of action
    turn = coefficient * int(action[1:])
    
    # save oldpos for buffer and get newpos
    oldposition = position
    position += turn
    
    # if out of bounds, put it back, and if not starting
    # or ending on 0, then rotation goes thru 0
    while position > 99:
        position -= 100
        if position != 0:
            turnedThroughZero += 1
    while position < 0:
        position += 100
        if position != 0 and oldposition != 0 and turn<-100:
            turnedThroughZero += 1
    # after every turn, we check if we are at 0
    if position == 0:
        zeroes+=1
        if verbose:
            print(f"The dial is rotated {action} to point at {position}!!!",end='')
    else:
        if verbose:
            print(f"The dial is rotated {action} to point at {position}.",end='')
    zeroes += turnedThroughZero
    if turnedThroughZero > 0:
        if verbose:
            print(f" During this rotation, it points at zero {turnedThroughZero} times.")
    else:
        if verbose:
            print(f"")

print(f"The safe code points at 0 a total of {zeroes} times. (part 2.2)")