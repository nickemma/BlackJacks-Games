import random


def get_choices():
    player_choice = input('enter a choice(rock, Paper, scissors: )')
    options = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(options)
    choices = {"player": player_choice, "computer": computer_choice}
    return choices


def check_win(player, computer):
    print(f"you chose {player} and computer chose {computer}")
    if player == computer:
        return "it's a tie"
    elif player == 'rock':
        if computer == 'scissors':
            return "rock smashes scissors. you win"
        else:
            return "scissors cuts paper. you lose"
    elif player == 'paper':
        if computer == 'rock':
            return "paper covers rock. you win"
        else:
            return "rock smashes scissor. you lose"
    elif player == 'scissors':
        if computer == 'paper':
            return "rock smashes scissors. you win"
        else:
            return "paper covers rock. you lose"


response = get_choices()
result = check_win(response["player"], response['computer'])
print(result)
