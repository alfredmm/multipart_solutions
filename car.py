correct_guess = 42500
count = 0
limit = 5

while count<limit:
    guess = int(input('Guess the car price : '))
    count += 1
    print("You have ", limit-count, "trials remaining...")

    if guess == correct_guess:
        print('Congratulations! You got it!')
        break
    elif guess > correct_guess:
        print("Guess is too high!")
    else:
        print("Guess is too low!")
else:
    print('Exceeded the guess limit')

while True:
    ans = input("Guess:")
    if ans == 42500:
        break
    else:
        print("Keep guessing")
        print("You entered",ans)