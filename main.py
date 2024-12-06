import random, time

def rand_num():
    return random.randint(1,100)


def logic(num_to_guess, user_num, tries, tries_count):
    if user_num == num_to_guess:
        print(f'You guessed the number in {tries_count} tries! Congratulations! \n')
        return True

    if tries_count >= tries:
        print(f'You did not guess the number in {tries} tries. The correct number was {num_to_guess}.\n')
        return True

    if tries - tries_count == 1:
        print(f'Hint! The number is {"even" if num_to_guess % 2 == 0 else "odd"}')

    if user_num < num_to_guess:
        print('My number is bigger.\n')
        return False
    elif user_num > num_to_guess:
        print('My number is smaller.\n')
        return False


def main():
    print('\nWelcome to the Number Guessing Game!\n')
    print('I\'m thinking of a number between 1 and 100.\n')

    print('Please select the difficulty level:')
    print(' 1. Easy (10 chances) \n 2. Medium (5 chances) \n 3. Hard (3 chances) \n')
    
    while True:
        user_difficulty = input('Enter your choice: ')

        try:
            user_difficulty = int(user_difficulty)
            if user_difficulty in (1, 2, 3):
                break
            else:
                print('Invalid choice. Please enter 1, 2, or 3.\n')
        except ValueError:
            print('Invalid input. Please enter a number (1, 2, or 3).\n')

    print(f'Great! You have selected the {user_difficulty} difficulty level.\n')
    print('Let\'s start the game!\n')

    tries_count = 0
    tries = {1: 10, 2: 5, 3: 3}[user_difficulty]

    num_to_guess = rand_num()
    t0 = time.time() 

    while tries_count < tries:
        user_num = input('Enter your guess: ')

        try:
            user_num = int(user_num)
            if 1 <= user_num <= 100:
                tries_count += 1
                game_over = logic(num_to_guess, user_num, tries, tries_count)
                if game_over:
                    break
            else:
                print('Invalid choice. Please enter a number between 1 and 100.\n')
        except ValueError:
            print('Invalid input. Please enter a number between 1 and 100.\n')

    t1 = time.time() 
    print('Game over\n')
    
    mins = round((t1 - t0) / 60)
    sec = round((t1 - t0) % 60)
    print(f'The attempt took you {mins} minutes and {sec} seconds')

    print('============================================================')

   
while True:
    print('Want to play?\n\n')
    print('1. Yes\n2. No')
    end_or_cont = input('Enter your choice (1 or 2): ')
    if end_or_cont == '1':
        main()
    elif end_or_cont == '2':
        break