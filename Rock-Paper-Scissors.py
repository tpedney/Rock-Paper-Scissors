import random

moves = {
    'rock':{
        'win': 'scissors',
        'lose': 'paper',
    },
    'paper':{
        'win': 'rock',
        'lose': 'scissors',
    },
    'scissors':{
        'win': 'paper',
        'lose': 'rock',
    }
}

def update_score(user_name, score):
    with open('rating.txt', 'r') as new_file:
        for line in new_file:
            if user_name in line:
                print(f'Your rating: {player["score"]}')

print('Enter your name: ')
user_name = input()
print(f'Hello, {user_name}')

player = {'name': user_name, 'score':0}
with open('rating.txt', 'r') as new_file:
    for line in new_file:
        name, user_score = line.strip().split()
        if user_name.lower() == name.lower():
            player['score'] = int(user_score)
            break

score =player['score']

while True:
    user_answer = input()
    possible_ans = ['scissors', 'paper', 'rock']
    random_ans = random.choice(possible_ans)
    if user_answer == "!exit":
        print("Bye!")
        break
    if user_answer == "!rating":
        print(f'Your rating: {score}')
        continue
    if user_answer not in possible_ans:
        print("Invalid input")
        continue
        
    if user_answer == random_ans:
        print(f'There is a draw ({user_answer})')
        score += 50

    if moves[user_answer]['win'] == random_ans:
        print(f'Well done. The computer chose {random_ans} and failed')
        score += 100

    if moves[user_answer]['lose'] == random_ans:
        print(f'Sorry, but the computer chose {random_ans}')
player['score'] = score          