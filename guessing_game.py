import sys
from random import randint

start = int(sys.argv[1])
end = int(sys.argv[2])

answer = randint(start, end)
print(answer)


while True:
    guess = int(input(f'Please guess a number between {start} and {end}: '))

    if guess in range(start, end + 1):
        if guess == answer:
            print('Correct!')
            break
    else:
        print('Please pick a valid number')
