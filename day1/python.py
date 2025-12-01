#only part TWO

dial = 50
dialCount = 0

with open("rotations.txt") as rotations:
    for rotation in rotations:
        rotation = rotation.strip()
        if not rotation:
            continue
        direction = rotation[0]
        distance = int(rotation[1:])

        if (direction == 'L'):
            for i in range(distance):
                dial -= 1
                if (dial < 0):
                    dial = 99
                if (dial == 0):
                    dialCount += 1

        if (direction == 'R'):
            for i in range(distance):
                dial += 1
                if (dial > 99):
                    dial = 0
                if (dial == 0):
                    dialCount += 1

print(f"Final dial count is: {dialCount}")
print(f"Final dial number is: {dial}")
