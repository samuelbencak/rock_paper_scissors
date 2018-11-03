import random

def input_human_play(input=input):
    play = input('rock, paper, or scissors?')
    while not is_valid_play(play):
        play = input('rock, paper, or scissors?')
    return play

def is_valid_play(play):
#    return True
    return play in ['rock','paper', 'scissors']

def generate_computer_play():
    return random.choice(['rock', 'paper', 'scissors'])

def evaluate_game(human, computer):
    if human == computer:
        return 'tie'
    elif (computer == 'rock' and human == 'paper'):
        return 'human'
    elif (computer == 'paper' and human == 'rock'):
        return 'computer'
    elif (computer == 'scissors' and human == 'rock'):
        return 'human'
    elif (computer == 'rock' and human == 'scissors'):
        return 'computer'
    elif (computer == 'scissors' and human == 'paper'):
        return 'computer'
    elif (computer == 'paper' and human == 'scissors'):
        return 'human'

def main(input=input):
    human = input_human_play(input)
    computer = generate_computer_play()

    print(computer)

    game = evaluate_game(human, computer)
    if game == 'tie':
        print ("it is a tie")
    else:
        print(f'{game} won')

if __name__ == '__main__':
    main()
