def list_cards():
    if dic:
        for q in dic:
            print(f"\nQuestion: {q}")
            print('Please press "y" to see the answer or press "n" to skip:')
            if input() == 'y':
                print(f"\nAnswer: {dic[q]}")
    else:
        print('\nThere is no flashcard to practice!')

def add_cards():
    while True:
        print(menu2)
        cmd = input()
        if cmd == '1':
            new_cards()
        elif cmd == '2':
            break
        else:
            print(f'\n{cmd} is not an option')

def new_cards():
    while True:
        q = input('\nQuestion:\n')
        if q.strip():
            break
    while True:
        a = input('Answer:\n')
        if a.strip():
            break
    dic[q] = a


menu1 = '''
1. Add flashcards
2. Practice flashcards
3. Exit'''

menu2 = '''
1. Add a new flashcard
2. Exit'''

dic = {}

while True:
    print(menu1)
    cmd = input()
    if cmd == '1':
        add_cards()
    elif cmd == '2':
        list_cards()
    elif cmd == '3':
        break
    else:
        print(f'{cmd} is not an option')

print('Bye!')
