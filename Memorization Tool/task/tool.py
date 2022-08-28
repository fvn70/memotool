from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
engine = create_engine('sqlite:///flashcard.db?check_same_thread=False')
Session = sessionmaker(bind=engine)
session = Session()

class Card(Base):
    __tablename__ = 'flashcard'

    id = Column(Integer, primary_key=True)
    question = Column(String)
    answer = Column(String)

def list_cards():
    rows = session.query(Card).all()
    if rows:
        for r in rows:
            print(f"\nQuestion: {r.question}")
            while True:
                print(menu3)
                cmd = input()
                if cmd == 'y':
                    print(f"\nAnswer: {r.answer}")
                    break
                elif cmd == 'u':
                    upd_card(r)
                    break
                elif cmd == 'n':
                    break
                else:
                    print(f'\n{cmd} is not an option')
    else:
        print('\nThere is no flashcard to practice!')


def upd_card(card):
    while True:
        print(menu4)
        cmd = input()
        if cmd == 'd':
            del_card(card)
        elif cmd == 'e':
            edit_card(card)
        else:
            print(f'\n{cmd} is not an option')
            continue
        break

def del_card(card):
    session.delete(card)
    session.commit()

def edit_card(card):
    print(f'current question: {card.question}')
    q = input('please write a new question:\n')
    print(f'current answer: {card.answer}')
    a = input('please write a new answer:\n')
    if q.strip():
        card.question = q
    if a.strip():
        card.answer = a
    session.commit()

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
    card = Card(question=q, answer=a)
    session.add(card)
    session.commit()


menu1 = '''
1. Add flashcards
2. Practice flashcards
3. Exit'''

menu2 = '''
1. Add a new flashcard
2. Exit'''

menu3 = '''press "y" to see the answer:
press "n" to skip:
press "u" to update:
'''

menu4 = '''press "d" to delete the flashcard:
press "e" to edit the flashcard:
'''

Base.metadata.create_all(engine)

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

session.close()
print('Bye!')
