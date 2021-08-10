secret_number = 7
guess_limit = 3
guess_count = 0

while guess_count < guess_limit:
    guess_number = int(input('Guess: '))
    guess_count += 1
    if secret_number == guess_number:
        print('you win')
        break
else:   # this else block will execute after while loop
    print('you lose')
